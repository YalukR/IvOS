# IvOS

> Una distro basada en Arch Linux, ligera, pensada para estudiantes y
> profesionistas de LATAM que sacan adelante su carrera con equipo
> que ya no da para mucho.

Nace de una necesidad real: terminar la carrera (o el trabajo) con una
laptop de 8-10 años, sin presupuesto para algo mejor, y sin que instalar
las herramientas de tu área sea un calvario.

## La idea central

1. Instalas IvOS (instalador basado en `archinstall`).
2. Al primer arranque corre `ivos-instalador.sh`.
3. Te pregunta qué área estudias/trabajas (puedes elegir varias):
   Arquitectura, Programación, Biología/Biotecnología, Diseño gráfico.
4. Te muestra la lista EXACTA de paquetes que va a instalar (separados
   en repos oficiales vs AUR).
5. Confirmas, y solo entonces instala. Nada se mete sin que lo veas.

## Estructura del repo

```
ivos/
├── packages/          # Listas de paquetes por carrera (1 paquete por linea, prefijo [AUR] si aplica)
│   ├── arquitectura.txt
│   ├── programacion.txt
│   ├── biologia.txt
│   └── diseno.txt
├── scripts/
│   └── ivos-instalador.sh   # TUI que pregunta carrera y instala (whiptail + pacman/AUR helper)
├── branding/          # Wallpapers, logo, tema GRUB/SDDM (pendiente)
└── docs/              # Notas y roadmap
```

## Cómo construir la ISO (en tu Arch Linux)

IvOS se construye con `archiso`, la herramienta oficial de Arch para
generar la ISO de instalación.

### 1. Preparar el entorno

```bash
sudo pacman -S archiso git
```

### 2. Crear el perfil base

```bash
cp -r /usr/share/archiso/configs/releng/ ivos-build
cd ivos-build
```

`releng` es el perfil que usa Arch para su propia ISO oficial — es el
punto de partida más estable.

### 3. Agregar paquetes al perfil (KDE Plasma minimo + whiptail)

Edita `packages.x86_64` y agrega al final:

```
plasma-desktop
sddm
konsole
dolphin
sudo
networkmanager
libnewt
git
```

(Evita `plasma-meta`/`kde-applications-meta` completos para no inflar
la ISO — agrega solo lo esencial de Plasma.)

### 4. Meter el instalador de IvOS dentro de la imagen

```bash
mkdir -p airootfs/usr/local/bin
cp ../ivos/scripts/ivos-instalador.sh airootfs/usr/local/bin/
chmod +x airootfs/usr/local/bin/ivos-instalador.sh

mkdir -p airootfs/usr/local/share/ivos/packages
cp ../ivos/packages/*.txt airootfs/usr/local/share/ivos/packages/
```

El script ya respeta la variable `IVOS_PKG_DIR`, así que en el
servicio de primer arranque (ver paso 5) exporta:

```bash
export IVOS_PKG_DIR=/usr/local/share/ivos/packages
```

### 5. Hacer que corra en el primer arranque

Pendiente: crear un servicio systemd `ivos-first-boot.service` que
dispare el script una sola vez tras el primer login, y se desactive
solo después. (Ver TODO en docs/ROADMAP.md)

### 6. Construir

```bash
sudo mkarchiso -v -o out/ .
```

Esto genera un `.iso` en `out/`. Pruébalo SIEMPRE primero en una VM
(QEMU/VirtualBox) antes de grabarlo en un USB real.

```bash
qemu-system-x86_64 -enable-kvm -m 2048 -cdrom out/*.iso -boot d
```

## Roadmap (ver docs/ROADMAP.md)

- [x] Listas de paquetes por carrera (v1: 4 áreas, Arch/AUR)
- [x] Script instalador interactivo (whiptail + pacman/AUR helper)
- [ ] Branding: wallpaper + logo + tema GRUB/SDDM
- [ ] Servicio systemd para correr el instalador en primer arranque
- [ ] Perfil archiso completo y probado
- [ ] Decidir AUR helper a incluir por defecto (yay vs paru)
- [ ] Página/repo con instrucciones de instalación para usuario final

## Nota sobre ser rolling release

Arch es rolling release: no hay "versiones" fijas como en Debian, los
paquetes se actualizan continuamente. Para una distro pensada en gente
no técnica, esto es un riesgo real (una laptop que no se actualiza en
meses puede tener una actualización conflictiva). Mitigaciones a
considerar más adelante: recordatorios de actualización frecuente,
o fijar versiones de paquetes críticos.
