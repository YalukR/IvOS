#!/usr/bin/env bash
# Lanza IvOS Installer desde el codigo fuente (modo desarrollo).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
python3 -m ivos_installer.main "$@"
