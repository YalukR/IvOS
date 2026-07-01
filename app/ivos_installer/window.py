"""Ventana principal de IvOS Installer: un Gtk.Stack de 4 pasos.

Bienvenida -> Seleccion de perfil -> Resumen/confirmacion -> Progreso
"""

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, GLib, Gtk  # noqa: E402

from .packages import InstallPlan, build_install_plan, run_install_plan
from .pages.profile_select import ProfileSelectPage
from .pages.progress import ProgressPage
from .pages.summary import SummaryPage
from .pages.welcome import build_welcome_page
from .profiles import PROFILES

PAGE_WELCOME = "welcome"
PAGE_PROFILES = "profiles"
PAGE_SUMMARY = "summary"
PAGE_PROGRESS = "progress"

# En que paginas tiene sentido mostrar el boton de "Atras"
PAGES_WITH_BACK = {PAGE_PROFILES, PAGE_SUMMARY}


class IvosWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.set_title("IvOS Installer")
        self.set_default_size(720, 640)

        self._profiles_by_id = {p.id: p for p in PROFILES}

        self._header = Adw.HeaderBar()
        self._back_button = Gtk.Button(icon_name="go-previous-symbolic")
        self._back_button.connect("clicked", lambda _btn: self._go_back())
        self._back_button.set_visible(False)
        self._header.pack_start(self._back_button)

        self._stack = Gtk.Stack()
        self._stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

        self._welcome_page = build_welcome_page(on_start=self._go_to_profiles)
        self._profile_page = ProfileSelectPage(PROFILES, on_continue=self._go_to_summary)
        self._summary_page = SummaryPage(on_confirm=self._start_install)
        self._progress_page = ProgressPage(on_finish=self._finish)

        self._stack.add_named(self._welcome_page, PAGE_WELCOME)
        self._stack.add_named(self._profile_page, PAGE_PROFILES)
        self._stack.add_named(self._summary_page, PAGE_SUMMARY)
        self._stack.add_named(self._progress_page, PAGE_PROGRESS)

        toolbar_view = Adw.ToolbarView()
        toolbar_view.add_top_bar(self._header)
        toolbar_view.set_content(self._stack)
        self.set_content(toolbar_view)

        self._show_page(PAGE_WELCOME)

    # --- Navegacion ----------------------------------------------------

    def _show_page(self, page_name: str) -> None:
        self._stack.set_visible_child_name(page_name)
        self._back_button.set_visible(page_name in PAGES_WITH_BACK)

    def _go_back(self) -> None:
        current = self._stack.get_visible_child_name()
        if current == PAGE_SUMMARY:
            self._show_page(PAGE_PROFILES)
        elif current == PAGE_PROFILES:
            self._show_page(PAGE_WELCOME)

    def _go_to_profiles(self) -> None:
        self._show_page(PAGE_PROFILES)

    def _go_to_summary(self, selected_profile_ids: list[str]) -> None:
        plan = build_install_plan(selected_profile_ids, self._profiles_by_id)
        self._summary_page.set_plan(plan)
        self._show_page(PAGE_SUMMARY)

    def _start_install(self, plan: InstallPlan | None) -> None:
        if plan is None or plan.is_empty:
            return

        self._back_button.set_visible(False)
        self._show_page(PAGE_PROGRESS)
        self._progress_page.start()

        def on_line(text: str) -> None:
            GLib.idle_add(self._progress_page.append_line, text)

        def on_done(success: bool) -> None:
            GLib.idle_add(self._progress_page.set_finished, success)

        run_install_plan(plan, on_line, on_done)

    def _finish(self) -> None:
        # Al terminar, regresamos a la seleccion de perfil por si el usuario
        # quiere instalar herramientas de otra area en la misma sesion.
        self._profile_page.reset()
        self._show_page(PAGE_PROFILES)
