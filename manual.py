from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import NoTransition, ScreenManager
from kivy.app import App

class ManualScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager(transition=NoTransition())

    def back_to_input(self):
        app = App.get_running_app()
        app.root.current = "input"