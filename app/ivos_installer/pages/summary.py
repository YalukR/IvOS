"""Pantalla de resumen: muestra exactamente que se va a instalar antes de tocar nada."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk  # noqa: E402

from ..packages import InstallPlan


class SummaryPage(Gtk.Box):
    def __init__(self, on_confirm) -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=18)
        self.set_margin_top(36)
        self.set_margin_bottom(36)
        self.set_margin_start(24)
        self.set_margin_end(24)

        self._on_confirm = on_confirm
        self._plan: InstallPlan | None = None

        title = Gtk.Label(label="Esto es lo que se va a instalar")
        title.add_css_class("title-1")
        self.append(title)

        self._groups_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        scroller = Gtk.ScrolledWindow()
        scroller.set_child(self._groups_box)
        scroller.set_vexpand(True)
        self.append(scroller)

        self._confirm_button = Gtk.Button(label="Confirmar e instalar")
        self._confirm_button.add_css_class("suggested-action")
        self._confirm_button.add_css_class("pill")
        self._confirm_button.set_halign(Gtk.Align.END)
        self._confirm_button.connect("clicked", lambda _btn: self._on_confirm(self._plan))
        self.append(self._confirm_button)

    def set_plan(self, plan: InstallPlan) -> None:
        self._plan = plan

        child = self._groups_box.get_first_child()
        while child is not None:
            next_child = child.get_next_sibling()
            self._groups_box.remove(child)
            child = next_child

        if plan.is_empty:
            empty_label = Gtk.Label(label="No se encontraron paquetes para esta selección.")
            empty_label.add_css_class("dim-label")
            self._groups_box.append(empty_label)
            self._confirm_button.set_sensitive(False)
            return

        self._confirm_button.set_sensitive(True)

        if plan.apt_packages:
            self._groups_box.append(
                self._build_group(f"Repositorios de Ubuntu ({len(plan.apt_packages)})", plan.apt_packages)
            )

        if plan.flatpak_ids:
            self._groups_box.append(
                self._build_group(f"Flatpak / Flathub ({len(plan.flatpak_ids)})", plan.flatpak_ids)
            )

    @staticmethod
    def _build_group(heading: str, items: list[str]) -> Gtk.Widget:
        group = Adw.PreferencesGroup(title=heading)
        list_box = Gtk.ListBox()
        list_box.add_css_class("boxed-list")
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        for item in items:
            list_box.append(Adw.ActionRow(title=item))
        group.add(list_box)
        return group
