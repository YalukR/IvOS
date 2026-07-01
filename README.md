# IvOS

**IvOS** es una distribución de Linux basada en Arch Linux, pensada para la comunidad académica: estudiantes y profesores que necesitan un sistema listo para trabajar sin perder tiempo configurando herramientas desde cero.

El nombre viene de mi propio nombre, Ivo — este proyecto nació como parte de mi portafolio personal, pero está construido para ser realmente usable, no solo una demo.

## ¿Qué la hace diferente?

La idea central de IvOS es simple: **el instalador pregunta quién eres antes de instalar software**.

En vez de entregar un sistema base genérico (o, en el otro extremo, una distro cargada de programas que nunca vas a usar), el instalador de IvOS pide el **perfil del usuario** — por ejemplo, si eres estudiante o profesor, y en qué área — y en base a eso preinstala el set de herramientas que realmente vas a necesitar.

Ejemplos de lo que esto podría significar (en construcción):

- **Perfil estudiante** → editores de código, entornos de programación, herramientas de oficina, lectores PDF, apps de organización/notas.
- **Perfil profesor** → herramientas de presentación, grabación/edición de clases, gestión de contenido, ofimática avanzada.
- Perfiles adicionales por área (ingeniería, diseño, ciencias, etc.) — *pendiente de definir*.

## Estado del proyecto

🚧 En desarrollo activo. Este repositorio contiene el trabajo en progreso: perfil de `archiso`, scripts de instalación, configuraciones y branding.

## Estructura del repositorio

```
IvOS/
├── archiso/                  # Profile de archiso usado para generar la ISO
├── installer/                 # Lógica del instalador y perfiles de usuario
├── pkgbuilds/                  # Paquetes propios (si aplica)
├── configs/                    # Dotfiles y configuraciones del sistema
├── branding/                   # Logo, wallpapers, tema visual
├── LICENSE
└── README.md
```

*(Esta estructura puede ir cambiando conforme avanza el proyecto.)*

## Instalación

> Aún no hay una ISO estable para descargar. Esta sección se actualizará cuando exista un primer release.

## Contribuir

Este es principalmente un proyecto personal/de portafolio, pero si eres parte de la comunidad académica y tienes ideas sobre qué herramientas deberían incluirse en cada perfil, los issues y pull requests son bienvenidos.

## Licencia

Este proyecto está licenciado bajo **GPLv3**. Ver [LICENSE](LICENSE) para el texto completo.

Ten en cuenta que IvOS se apoya en el ecosistema de Arch Linux y sus paquetes, cada uno con su propia licencia (mayormente GPL, MIT y BSD). La licencia GPLv3 de este repositorio aplica al trabajo propio del proyecto: scripts, configuraciones, el instalador y el branding.

## Aviso de marca

IvOS es una distribución basada en Arch Linux. **No está afiliada ni respaldada oficialmente por el proyecto Arch Linux.**

---

*Un proyecto de Ivo.*