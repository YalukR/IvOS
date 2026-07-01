"""Lectura de listas de paquetes y construccion del plan de instalacion.

Formato de las listas (packages/<perfil>.txt):
    - Una linea con `#` al inicio es un comentario, se ignora.
    - Una linea vacia se ignora.
    - `nombre-paquete`            -> paquete de apt (repos oficiales de Ubuntu)
    - `[FLATPAK] app.id.completo` -> paquete via Flatpak/Flathub
"""

from __future__ import annotations

import subprocess
import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

FLATPAK_PREFIX = "[FLATPAK]"


def repo_root() -> Path:
    """Sube desde app/ivos_installer/ hasta la raiz del repositorio."""
    return Path(__file__).resolve().parents[2]


def packages_dir() -> Path:
    return repo_root() / "packages"


@dataclass
class InstallPlan:
    apt_packages: list[str] = field(default_factory=list)
    flatpak_ids: list[str] = field(default_factory=list)
    profile_ids: list[str] = field(default_factory=list)

    @property
    def is_empty(self) -> bool:
        return not self.apt_packages and not self.flatpak_ids


def parse_package_file(path: Path) -> tuple[list[str], list[str]]:
    """Separa un archivo de lista en (paquetes_apt, ids_flatpak)."""
    apt_packages: list[str] = []
    flatpak_ids: list[str] = []

    if not path.is_file():
        return apt_packages, flatpak_ids

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(FLATPAK_PREFIX):
            flatpak_ids.append(line[len(FLATPAK_PREFIX):].strip())
        else:
            apt_packages.append(line)

    return apt_packages, flatpak_ids


def build_install_plan(profile_ids: Iterable[str], profiles_by_id: dict) -> InstallPlan:
    """Combina las listas de paquetes de uno o varios perfiles, sin duplicados."""
    apt_set: set[str] = set()
    flatpak_set: set[str] = set()
    selected: list[str] = []

    for profile_id in profile_ids:
        profile = profiles_by_id.get(profile_id)
        if profile is None:
            continue
        selected.append(profile_id)
        apt_pkgs, flatpak_pkgs = parse_package_file(packages_dir() / profile.package_file)
        apt_set.update(apt_pkgs)
        flatpak_set.update(flatpak_pkgs)

    return InstallPlan(
        apt_packages=sorted(apt_set),
        flatpak_ids=sorted(flatpak_set),
        profile_ids=selected,
    )


# --- Ejecucion de la instalacion -------------------------------------------

OnLine = Callable[[str], None]
OnDone = Callable[[bool], None]


def _run_streamed(command: list[str], on_line: OnLine) -> bool:
    """Corre un comando mostrando su salida linea por linea. True si tuvo exito."""
    on_line(f"$ {' '.join(command)}")
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
    except FileNotFoundError:
        on_line(f"  ✗ No se encontró el comando: {command[0]}")
        return False

    assert process.stdout is not None
    for line in process.stdout:
        on_line(line.rstrip())

    return process.wait() == 0


def run_install_plan(plan: InstallPlan, on_line: OnLine, on_done: OnDone) -> None:
    """Ejecuta el plan de instalacion en un hilo aparte para no congelar la UI.

    `on_line` y `on_done` deben usar GLib.idle_add si actualizan widgets GTK,
    ya que este hilo no corre en el hilo principal.
    """

    def worker() -> None:
        success = True

        if plan.apt_packages:
            on_line("== Instalando paquetes de los repositorios de Ubuntu ==")
            command = ["pkexec", "apt-get", "install", "-y", *plan.apt_packages]
            success = _run_streamed(command, on_line) and success

        if plan.flatpak_ids:
            on_line("== Instalando paquetes vía Flatpak/Flathub ==")
            for flatpak_id in plan.flatpak_ids:
                command = ["flatpak", "install", "-y", "flathub", flatpak_id]
                success = _run_streamed(command, on_line) and success

        on_done(success)

    threading.Thread(target=worker, daemon=True).start()
