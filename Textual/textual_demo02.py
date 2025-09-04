
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Header, Footer, Button, Static
from textual.screen import Screen


class ContentScreen(Screen):
    """Obrazovka, která uprostřed zobrazí název stisknutého tlačítka."""
    BINDINGS = [
        ("escape", "zpet", "Zpět")
    ]

    def __init__(self, label: str) -> None:
        super().__init__()
        self._label = label

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        # Kontejner vycentruje text na střed obrazovky.
        yield Container(
            Static(f"Obrazovka: {self._label}", id="center-label"),
            id="screen-body",
        )
        yield Footer()

    def action_zpet(self) -> None:
        """Vrátí se na předchozí obrazovku (menu)."""
        self.app.pop_screen()

    CSS = """
    #screen-body {
        height: 1fr;
        align: center middle;  /* Vycentruje obsah kontejneru */
    }

    #center-label {
        content-align: center middle;  /* Vycentruje text v rámci widgetu */
        padding: 2;
        border: round $boost;
    }
    """


class MenuApp(App):
    """Hlavní aplikace s hlavičkou, patičkou a levým tlačítkovým menu."""
    CSS = """
    Screen {
        layout: vertical;   /* Header | Tělo | Footer */
    }

    /* Tělo aplikace: vlevo menu, vpravo uvítací plocha */
    #main-row {
        height: 1fr;
        layout: horizontal;
    }

    /* Levý panel s tlačítky */
    #menu {
        width: 28;
        min-width: 22;
        max-width: 36;
        border: panel $secondary;
        padding: 1 1;
    }

    #menu Button {
        width: 100%;
        margin: 1 0;
    }

    /* Pravá uvítací plocha */
    #welcome {
        border: panel;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="main-row"):
            with Vertical(id="menu"):
                yield Static("Menu", classes="menu-title")
                # >>> Zde upravte seznam položek menu podle potřeby <<<
                for label in ["Dashboard", "Reporty", "Nastaveni", "Napoveda"]:
                    yield Button(label, id=f"btn-{label.lower()}")
            yield Static(
                "Stiskněte tlačítko vlevo pro otevření obrazovky.",
                id="welcome",
            )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Po stisknutí tlačítka otevře Screen s názvem tlačítka uprostřed."""
        # Textual může vracet Rich text, ošetříme tedy bezpečně string
        label = getattr(event.button.label, "plain", event.button.label)
        self.push_screen(ContentScreen(label))


if __name__ == "__main__":
    MenuApp().run()
