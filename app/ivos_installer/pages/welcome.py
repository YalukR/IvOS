"""Pantalla de bienvenida: primer contacto del usuario con IvOS."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk  # noqa: E402


def build_welcome_page(on_start) -> Adw.StatusPage:
    """Adw.StatusPage es una clase final en libadwaita: no se puede heredar,
    asi que la construimos con una funcion en vez de una subclase."""
    page = Adw.StatusPage()
    page.set_icon_name("computer-symbolic")
    page.set_title("Bienvenido a IvOS")
    page.set_description(
        "Antes de instalar nada, cuéntanos qué estudias o en qué área "
        "trabajas. Así solo instalamos lo que realmente vas a usar."
    )

    start_button = Gtk.Button(label="Comenzar")
    start_button.add_css_class("suggested-action")
    start_button.add_css_class("pill")
    start_button.set_halign(Gtk.Align.CENTER)
    start_button.connect("clicked", lambda _btn: on_start())

    page.set_child(start_button)
    return page
