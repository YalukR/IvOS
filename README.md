# IvOS

**IvOS** es un instalador/post-install para Ubuntu LTS, pensado para la comunidad académica: estudiantes y profesores que necesitan un sistema listo para trabajar sin perder tiempo configurando herramientas desde cero.

El nombre viene de mi propio nombre, Ivo — este proyecto nació como parte de mi portafolio personal, pero está construido con la intención de ser realmente usable, no solo una demo.

## ¿Qué hace?

La idea central de IvOS es simple: **se pregunta el perfil del usuario antes de instalar software**.

En vez de entregar un sistema base genérico (o, en el otro extremo, cargado de programas que nunca vas a usar), IvOS pregunta si eres estudiante o profesor — y en qué área — y en base a eso instala el set de herramientas que realmente vas a necesitar.

Ejemplos de lo que esto podría significar (en construcción):

- **Perfil estudiante** → editores de código, entornos de programación, herramientas de oficina, lectores PDF, apps de organización/notas.
- **Perfil profesor** → herramientas de presentación, grabación/edición de clases, gestión de contenido, ofimática avanzada.
- Perfiles adicionales por área (ingeniería, diseño, ciencias, etc.) — *pendiente de definir*.

## Base y filosofía

IvOS toma **Ubuntu LTS** como base, priorizando estabilidad y compatibilidad de hardware sobre tener siempre lo último. La idea es que un profesor o estudiante pueda instalar y olvidarse — no lidiar con actualizaciones que rompan el sistema justo antes de una clase.

Por defecto, IvOS evita Snap en favor de paquetes `.deb` estándar y/o Flatpak para software adicional, para mantener el sistema predecible y transparente.

## Estado del proyecto

En desarrollo activo. Ahora mismo IvOS es principalmente un **conjunto de scripts de instalación/configuración** que corren sobre una instalación de Ubuntu LTS existente — no una ISO propia (todavía). Empaquetarlo como ISO instalable es una posibilidad a futuro, no una prioridad actual.

## Estructura del repositorio

```
IvOS/
├── scripts/        # Lógica del instalador y perfiles de usuario
├── packages/        # Listas/definiciones de paquetes por perfil
├── docs/             # Documentación del proyecto
├── LICENSE
└── README.md
```

*(Esta estructura puede ir cambiando conforme avanza el proyecto.)*

## Uso

> El proyecto está en desarrollo temprano. Esta sección se actualizará con instrucciones claras de instalación conforme el instalador tome forma.

## Contribuir

Este es principalmente un proyecto personal/de portafolio, pero si eres parte de la comunidad académica y tienes ideas sobre qué herramientas deberían incluirse en cada perfil, los issues y pull requests son bienvenidos.

## Licencia

Este proyecto está licenciado bajo **GPLv3**. Ver [LICENSE](LICENSE) para el texto completo.

IvOS se apoya en el ecosistema de Ubuntu y sus paquetes, cada uno con su propia licencia. La licencia GPLv3 de este repositorio aplica al trabajo propio del proyecto: scripts, configuraciones, el instalador y el branding.

## Aviso de marca

IvOS está basado en Ubuntu. **No está afiliado ni respaldado oficialmente por Canonical Ltd. ni por el proyecto Ubuntu.**

---

*Un proyecto de Ivo.*