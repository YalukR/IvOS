#!/usr/bin/env bash
#
# IvOS - Instalador de herramientas por carrera (Arch Linux)
# Pregunta al usuario que estudia y muestra/instala las herramientas
# correspondientes, pidiendo confirmacion explicita antes de tocar nada.
#
# Requiere: whiptail
# Recomendado: un AUR helper (yay o paru) para paquetes marcados [AUR]
#
set -euo pipefail

PKG_DIR="${IVOS_PKG_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../packages" && pwd)}"

if ! command -v whiptail >/dev/null 2>&1; then
    echo "whiptail no esta instalado. Instalalo con: sudo pacman -S libnewt"
    exit 1
fi

# Detectar AUR helper disponible
AUR_HELPER=""
if command -v yay >/dev/null 2>&1; then
    AUR_HELPER="yay"
elif command -v paru >/dev/null 2>&1; then
    AUR_HELPER="paru"
fi

# --- Paso 1: seleccionar una o varias carreras ---
SELECCION=$(whiptail --title "Bienvenido a IvOS" \
    --checklist "¿Qué área estudias o en qué trabajas? (usa ESPACIO para elegir, una o varias)" \
    18 70 4 \
    "arquitectura" "Arquitectura (CAD, render, GIS)" OFF \
    "programacion" "Programación / Desarrollo" OFF \
    "biologia" "Biología / Biotecnología" OFF \
    "diseno" "Diseño gráfico / Multimedia" OFF \
    3>&1 1>&2 2>&3) || { echo "Cancelado por el usuario."; exit 0; }

if [ -z "$SELECCION" ]; then
    whiptail --msgbox "No seleccionaste ninguna área. Saliendo sin instalar nada." 8 60
    exit 0
fi

SELECCION=$(echo "$SELECCION" | tr -d '"')

# --- Paso 2: armar listas separadas: oficiales vs AUR ---
TMP_OFICIALES=$(mktemp)
TMP_AUR=$(mktemp)
for AREA in $SELECCION; do
    LISTFILE="$PKG_DIR/${AREA}.txt"
    if [ -f "$LISTFILE" ]; then
        grep -v '^\s*#' "$LISTFILE" | grep -v '^\s*$' | while read -r LINE; do
            if [[ "$LINE" == \[AUR\]* ]]; then
                echo "${LINE#\[AUR\] }" >> "$TMP_AUR"
            else
                echo "$LINE" >> "$TMP_OFICIALES"
            fi
        done
    fi
done

PAQUETES_OFICIALES=$(sort -u "$TMP_OFICIALES" 2>/dev/null || true)
PAQUETES_AUR=$(sort -u "$TMP_AUR" 2>/dev/null || true)
rm -f "$TMP_OFICIALES" "$TMP_AUR"

if [ -z "$PAQUETES_OFICIALES" ] && [ -z "$PAQUETES_AUR" ]; then
    whiptail --msgbox "No se encontraron paquetes para esa selección." 8 60
    exit 0
fi

# --- Paso 3: mostrar la lista completa y pedir confirmacion ---
TOTAL_OF=$(echo "$PAQUETES_OFICIALES" | grep -c . || true)
TOTAL_AUR=$(echo "$PAQUETES_AUR" | grep -c . || true)

TEXTO="Para las áreas seleccionadas ($SELECCION):\n\n"
TEXTO+="Repos oficiales ($TOTAL_OF):\n"
TEXTO+="$(echo "$PAQUETES_OFICIALES" | sed 's/^/  - /')\n\n"

if [ "$TOTAL_AUR" -gt 0 ]; then
    if [ -z "$AUR_HELPER" ]; then
        TEXTO+="AUR ($TOTAL_AUR) -- NO SE INSTALARAN, no hay yay/paru instalado:\n"
    else
        TEXTO+="AUR ($TOTAL_AUR) via $AUR_HELPER:\n"
    fi
    TEXTO+="$(echo "$PAQUETES_AUR" | sed 's/^/  - /')\n\n"
fi

TEXTO+="¿Confirmas la instalación?"

whiptail --title "Esto es lo que se va a instalar" --yesno "$TEXTO" 28 74

if [ $? -ne 0 ]; then
    echo "Instalación cancelada por el usuario."
    exit 0
fi

# --- Paso 4: instalar ---
if [ -n "$PAQUETES_OFICIALES" ]; then
    echo "Instalando paquetes oficiales..."
    # shellcheck disable=SC2086
    sudo pacman -Syu --needed --noconfirm $PAQUETES_OFICIALES
fi

if [ "$TOTAL_AUR" -gt 0 ]; then
    if [ -n "$AUR_HELPER" ]; then
        echo "Instalando paquetes AUR con $AUR_HELPER..."
        # shellcheck disable=SC2086
        $AUR_HELPER -S --needed --noconfirm $PAQUETES_AUR
    else
        echo "Aviso: se omitieron paquetes AUR porque no hay yay/paru instalado."
        echo "Instala uno y vuelve a correr este script si los necesitas."
    fi
fi

whiptail --msgbox "¡Listo! Se instalaron las herramientas para: $SELECCION" 8 60
echo "Instalación completada."
