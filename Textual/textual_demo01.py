from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Button
from textual.screen import Screen

class DashboardScreen(Screen):
    """Obrazovka pro 'Dashboard'"""
    
    def on_mount(self) -> None:
        self.update("[b]Dashboard[/b]\n\nToto je hlavní obrazovka.")

class SettingsScreen(Screen):
    """Obrazovka pro 'Nastavení'"""
    
    def on_mount(self) -> None:
        self.update("[b]Nastavení[/b]\n\nTady můžeš změnit různé možnosti.")

class AboutScreen(Screen):
    """Obrazovka pro 'O aplikaci'"""
    
    def on_mount(self) -> None:
        self.update("[b]O aplikaci[/b]\n\nTato aplikace je napsaná v Pythonu pomocí knihovny Textual.")

class MainApp(App):
    CSS_PATH = None  # Nepoužíváme externí CSS

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                Button("Dashboard", id="dashboard", variant="primary"),
                Button("Nastavení", id="settings", variant="primary"),
                Button("O aplikaci", id="about", variant="primary"),
                Button("Ukončit", id="exit", variant="error"),  # Tlačítko pro ukončení
                id="menu",
            ),
            Container(id="content")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Změní obrazovku nebo ukončí aplikaci podle stisknutého tlačítka"""
        if event.button.id == "dashboard":
            self.push_screen(DashboardScreen)
        elif event.button.id == "settings":
            self.push_screen(SettingsScreen)
        elif event.button.id == "about":
            self.push_screen(AboutScreen)
        elif event.button.id == "exit":
            self.exit()  # Ukončení aplikace

if __name__ == "__main__":
    MainApp().run()
