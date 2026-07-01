# Roadmap de IvOS

Este documento describe el plan de desarrollo de IvOS, desde su forma actual (un instalador de herramientas) hasta convertirse en una distribución completa con ISO propia.

El desarrollo es incremental por diseño: cada fase construye sobre la anterior sin necesidad de tirar trabajo previo.

---

## Fase 1 — Scripts de instalación por perfil

Lógica base en Bash que pregunta el área académica del usuario y instala las herramientas correspondientes, con confirmación explícita antes de tocar el sistema.

- [x] Script de instalación interactivo (originalmente con `whiptail`)
- [x] Listas de paquetes por área (arquitectura, programación, biología, diseño)
- [x] Separación de paquetes oficiales vs. AUR *(en migración a apt/Flatpak)*

## Fase 2 — App gráfica (GTK4 + libadwaita) — *fase actual*

Reemplazo de la interfaz de terminal por una aplicación de escritorio real, con estética nativa de GNOME.

- [ ] Migrar listas de paquetes de `pacman`/AUR a `apt`/Flatpak
- [ ] Pantalla de bienvenida
- [ ] Pantalla de selección de perfil (checkboxes, uno o varios)
- [ ] Pantalla de resumen y confirmación
- [ ] Pantalla de progreso de instalación (salida en vivo)
- [ ] Manejo de errores (paquete no encontrado, sin conexión, etc.)

## Fase 3 — Integración al flujo de instalación de Ubuntu

Que la app de IvOS no sea algo que el usuario tenga que buscar y abrir manualmente, sino parte natural del proceso de "instalar y usar".

- [ ] Evaluar integración vía first-boot (oem-config/casper) — la app corre automáticamente en el primer arranque
- [ ] Evaluar integración directa al instalador de Ubuntu (Subiquity) como paso adicional
- [ ] Definir cuál enfoque es más viable para mantener a largo plazo

## Fase 4 — ISO propia (`live-build`)

El salto de "instalador/app sobre Ubuntu" a "distribución descargable".

- [ ] Configurar entorno de `live-build` (o evaluar Cubic como alternativa más visual)
- [ ] Definir paquete base de IvOS (Ubuntu LTS + GNOME + apps esenciales)
- [ ] Preinstalar la app de IvOS en la imagen
- [ ] Generar primer build de prueba de la ISO
- [ ] Documentar proceso de build para reproducibilidad

## Fase 5 — Identidad visual y branding completo

El detalle que hace que se sienta una distro propia y no "Ubuntu con una app".

- [ ] Wallpapers propios
- [ ] Tema GNOME personalizado (o ajustes sobre el tema por defecto)
- [ ] Splash de arranque (Plymouth) con logo de IvOS
- [ ] Actualizar `/etc/os-release`, ícono en "Acerca de este equipo", nombre del sistema
- [ ] Ícono/logo oficial del proyecto

## Ideas a futuro (sin fecha)

- Web/landing page del proyecto
- Página de descarga con checksums de la ISO
- Más perfiles académicos (ingeniería, ciencias, idiomas, etc.)
- Modo "mínimo" para usuarios que no quieran ningún perfil preinstalado

---

*Este roadmap es una guía, no un contrato — puede reordenarse conforme el proyecto avance.*