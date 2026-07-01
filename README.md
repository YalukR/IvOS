# IvOS

**IvOS** es una distribución de Linux basada en Ubuntu LTS + GNOME, pensada para la comunidad académica: estudiantes y profesores que necesitan un sistema listo para trabajar sin perder tiempo configurando herramientas desde cero.

El nombre viene de mi propio nombre, Ivo — este proyecto nació como parte de mi portafolio personal, pero está construido con la intención de ser realmente usable, no solo una demo.

## ¿Qué hace?

La idea central de IvOS es simple: **se pregunta el perfil del usuario antes de instalar software**.

En vez de entregar un sistema base genérico (o, en el otro extremo, cargado de programas que nunca vas a usar), IvOS pregunta si eres estudiante o profesor — y en qué área — y en base a eso instala el set de herramientas que realmente vas a necesitar.

Ejemplos de lo que esto podría significar (en construcción):

- **Perfil estudiante** → editores de código, entornos de programación, herramientas de oficina, lectores PDF, apps de organización/notas.
- **Perfil profesor** → herramientas de presentación, grabación/edición de clases, gestión de contenido, ofimática avanzada.
- Perfiles adicionales por área (ingeniería, diseño, ciencias, etc.) — *pendiente de definir*.

## Base y filosofía

IvOS toma **Ubuntu LTS** como base y **GNOME** como entorno de escritorio, priorizando estabilidad, consistencia visual y "cero necesidad de andarle moviendo" por encima de la personalización extrema. La idea es que un profesor o estudiante pueda instalar y olvidarse — no lidiar con actualizaciones que rompan el sistema justo antes de una clase, ni con configuraciones que tenga que ajustar a mano.

Por defecto, IvOS evita Snap en favor de paquetes `.deb` estándar y/o Flatpak para software adicional, para mantener el sistema predecible y transparente.

## Estado del proyecto

En desarrollo activo. IvOS es un proyecto de portafolio con la ambición de convertirse en una distribución completa (ISO propia), construido de forma incremental. Ver [ROADMAP.md](docs/ROADMAP.md) para el plan completo por fases y en qué fase está el proyecto ahora mismo.

## Estructura del repositorio

```
IvOS/
├── app/            # App gráfica (GTK4/libadwaita) de selección de perfil e instalación
├── packages/        # Listas de paquetes por perfil académico
├── iso/               # Configuración para generar la ISO propia (live-build)
├── branding/           # Logo, wallpapers, tema, splash de arranque
├── docs/
│   └── ROADMAP.md        # Plan de desarrollo por fases
├── LICENSE
└── README.md
```

*(Esta estructura se irá llenando conforme avanza cada fase del roadmap.)*

## Uso

> El proyecto está en desarrollo temprano. Esta sección se actualizará con instrucciones claras de instalación conforme el instalador/distro tome forma.

## Contribuir

Este es principalmente un proyecto personal/de portafolio, pero si eres parte de la comunidad académica y tienes ideas sobre qué herramientas deberían incluirse en cada perfil, los issues y pull requests son bienvenidos.

## Licencia

Este proyecto está licenciado bajo **GPLv3**. Ver [LICENSE](LICENSE) para el texto completo.

IvOS se apoya en el ecosistema de Ubuntu/GNOME y sus paquetes, cada uno con su propia licencia. La licencia GPLv3 de este repositorio aplica al trabajo propio del proyecto: scripts, la app, configuraciones y branding.

## Aviso de marca

IvOS está basado en Ubuntu y GNOME. **No está afiliado ni respaldado oficialmente por Canonical Ltd., el proyecto Ubuntu, ni la Fundación GNOME.**

---

*Un proyecto de Ivo.*