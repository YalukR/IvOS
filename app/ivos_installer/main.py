"""Punto de entrada de IvOS Installer."""

import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk  # noqa: E402

from .window import IvosWindow

APP_ID = "mx.ivo.IvosInstaller"


class IvosApplication(Adw.Application):
    def __init__(self) -> None:
        super().__init__(application_id=APP_ID)

    def do_activate(self) -> None:
        window = self.props.active_window
        if window is None:
            window = IvosWindow(application=self)
        window.present()


def main() -> int:
    app = IvosApplication()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
