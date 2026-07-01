"""Pantalla de progreso: salida en vivo de la instalacion."""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, GLib, Gtk  # noqa: E402


class ProgressPage(Gtk.Box):
    def __init__(self, on_finish) -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=18)
        self.set_margin_top(36)
        self.set_margin_bottom(36)
        self.set_margin_start(24)
        self.set_margin_end(24)

        self._on_finish = on_finish

        self._title = Gtk.Label(label="Instalando…")
        self._title.add_css_class("title-1")
        self.append(self._title)

        self._progress_bar = Gtk.ProgressBar()
        self._progress_bar.set_show_text(False)
        self.append(self._progress_bar)

        self._text_view = Gtk.TextView()
        self._text_view.set_editable(False)
        self._text_view.set_monospace(True)
        self._text_view.set_cursor_visible(False)
        self._buffer = self._text_view.get_buffer()

        scroller = Gtk.ScrolledWindow()
        scroller.set_child(self._text_view)
        scroller.set_vexpand(True)
        scroller.add_css_class("card")
        self.append(scroller)

        self._finish_button = Gtk.Button(label="Listo")
        self._finish_button.add_css_class("pill")
        self._finish_button.set_halign(Gtk.Align.END)
        self._finish_button.set_visible(False)
        self._finish_button.connect("clicked", lambda _btn: self._on_finish())
        self.append(self._finish_button)

        self._pulse_source_id: int | None = None

    def start(self) -> None:
        self._title.set_label("Instalando…")
        self._buffer.set_text("")
        self._finish_button.set_visible(False)
        self._progress_bar.set_fraction(0.0)
        if self._pulse_source_id is None:
            self._pulse_source_id = GLib.timeout_add(200, self._pulse)

    def append_line(self, text: str) -> None:
        """Seguro de llamar desde el hilo de instalacion via GLib.idle_add."""
        end_iter = self._buffer.get_end_iter()
        self._buffer.insert(end_iter, text + "\n")
        self._text_view.scroll_to_iter(self._buffer.get_end_iter(), 0.0, False, 0.0, 0.0)

    def set_finished(self, success: bool) -> None:
        if self._pulse_source_id is not None:
            GLib.source_remove(self._pulse_source_id)
            self._pulse_source_id = None

        self._progress_bar.set_fraction(1.0)
        self._title.set_label("¡Listo!" if success else "Hubo un problema durante la instalación")
        self._finish_button.set_visible(True)

    def _pulse(self) -> bool:
        self._progress_bar.pulse()
        return True
