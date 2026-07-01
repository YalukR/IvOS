"""Pantalla de seleccion de perfil academico (una o varias areas)."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk  # noqa: E402

from ..profiles import Profile


class ProfileSelectPage(Gtk.Box):
    def __init__(self, profiles: list[Profile], on_continue) -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=18)
        self.set_margin_top(36)
        self.set_margin_bottom(36)
        self.set_margin_start(24)
        self.set_margin_end(24)

        self._on_continue = on_continue
        self._selected: set[str] = set()
        self._switch_rows: dict[str, Adw.SwitchRow] = {}

        title = Gtk.Label(label="¿Qué área estudias o en qué trabajas?")
        title.add_css_class("title-1")
        subtitle = Gtk.Label(
            label="Puedes elegir más de una. Siempre puedes instalar más herramientas después."
        )
        subtitle.add_css_class("dim-label")

        self.append(title)
        self.append(subtitle)

        list_box = Gtk.ListBox()
        list_box.add_css_class("boxed-list")
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        for profile in profiles:
            row = Adw.SwitchRow(title=profile.title, subtitle=profile.subtitle)
            row.set_icon_name(profile.icon_name)
            row.connect("notify::active", self._on_toggle, profile.id)
            list_box.append(row)
            self._switch_rows[profile.id] = row

        scroller = Gtk.ScrolledWindow()
        scroller.set_child(list_box)
        scroller.set_vexpand(True)
        self.append(scroller)

        self._continue_button = Gtk.Button(label="Continuar")
        self._continue_button.add_css_class("suggested-action")
        self._continue_button.add_css_class("pill")
        self._continue_button.set_halign(Gtk.Align.END)
        self._continue_button.set_sensitive(False)
        self._continue_button.connect("clicked", self._on_continue_clicked)
        self.append(self._continue_button)

    def _on_toggle(self, row: Adw.SwitchRow, _pspec, profile_id: str) -> None:
        if row.get_active():
            self._selected.add(profile_id)
        else:
            self._selected.discard(profile_id)
        self._continue_button.set_sensitive(bool(self._selected))

    def _on_continue_clicked(self, _button: Gtk.Button) -> None:
        self._on_continue(sorted(self._selected))

    def reset(self) -> None:
        """Limpia la seleccion, util si el usuario vuelve atras desde el resumen."""
        for row in self._switch_rows.values():
            row.set_active(False)
