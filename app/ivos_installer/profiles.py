"""Definicion de los perfiles academicos disponibles en IvOS.

Cada perfil apunta a un archivo de lista de paquetes en `packages/`,
relativo a la raiz del repositorio. Agregar un perfil nuevo es tan
simple como añadir una entrada aqui y su archivo .txt correspondiente.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    id: str
    title: str
    subtitle: str
    icon_name: str
    package_file: str


PROFILES: list[Profile] = [
    Profile(
        id="programacion",
        title="Programación / Desarrollo",
        subtitle="Editores, entornos de desarrollo, control de versiones",
        icon_name="applications-development-symbolic",
        package_file="programacion.txt",
    ),
    Profile(
        id="diseno",
        title="Diseño gráfico / Multimedia",
        subtitle="Edición de imagen, video, ilustración y audio",
        icon_name="applications-graphics-symbolic",
        package_file="diseno.txt",
    ),
    Profile(
        id="arquitectura",
        title="Arquitectura",
        subtitle="CAD, modelado 3D, renderizado y GIS",
        icon_name="applications-engineering-symbolic",
        package_file="arquitectura.txt",
    ),
    Profile(
        id="biologia",
        title="Biología / Biotecnología",
        subtitle="Análisis de datos, bioinformática y estadística",
        icon_name="applications-science-symbolic",
        package_file="biologia.txt",
    ),
]


def get_profile(profile_id: str) -> Profile | None:
    return next((p for p in PROFILES if p.id == profile_id), None)
