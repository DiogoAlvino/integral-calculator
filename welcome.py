from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import NoTransition, ScreenManager
from kivy.app import App

class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager(transition=NoTransition())

    def start_app(self):
        app = App.get_running_app()
        app.root.current = "input"