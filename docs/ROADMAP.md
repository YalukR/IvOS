# Roadmap de IvOS (Arch-based)

## v0.1 — Fundamentos (estado actual)
- [x] Definir identidad y nicho (Arch, estudiantes/profesionistas LATAM, hardware limitado)
- [x] Listas de paquetes por carrera: arquitectura, programación, biología, diseño (Arch/AUR)
- [x] Script instalador interactivo (whiptail) con confirmación explícita, soporte AUR

## v0.2 — Integración en la ISO
- [ ] Perfil completo de `archiso` basado en `releng` (carpeta versionada en el repo)
- [ ] Servicio systemd `ivos-first-boot.service` que lance el instalador
      una sola vez en el primer login (y se desactive solo después)
- [ ] Decidir si se incluye `yay` o `paru` preinstalado en la ISO
- [ ] Probar build completo en VM limpia

## v0.3 — Branding
- [ ] Logo de IvOS (simple, dos versiones: claro/oscuro)
- [ ] Wallpaper de bienvenida
- [ ] Tema GRUB/syslinux con nombre IvOS
- [ ] Pantalla SDDM personalizada
- [ ] `/etc/os-release` con nombre y versión propios

## v0.4 — Pulido de Plasma
- [ ] Configuración por defecto de KDE Plasma minimalista
      (sin widgets de sobra, menú simple, autostart limpio)
- [ ] Revisar consumo de RAM en frío (~objetivo: <800MB idle en 2GB RAM)

## v1.0 — Release pública
- [ ] ISO probada en al menos 2 equipos físicos reales (no solo VM)
- [ ] Documentación de instalación para usuario final (no técnico)
- [ ] Repo en GitHub con README pulido, capturas de pantalla, releases con ISO

## Ideas para después (no v1)
- Más disciplinas: medicina, ciencias sociales, contabilidad
- Mecanismo para mitigar riesgo de rolling release (recordatorios de update,
  o pin de versiones críticas)
- Modo "ultra ligero" sin entorno gráfico completo (solo lo esencial)
