from kivymd.app import MDApp
from kivy.uix.screenmanager import NoTransition
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.core.text import LabelBase
from input import InputScreen
from results import ResultScreen
from welcome import WelcomeScreen
from manual import ManualScreen

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.screen_manager = MDScreenManager(transition=NoTransition())

    def build(self):
        self.screen_manager.add_widget(WelcomeScreen())
        self.screen_manager.add_widget(ManualScreen())
        self.screen_manager.add_widget(InputScreen())
        self.screen_manager.add_widget(ResultScreen())
        return self.screen_manager
    
    def on_start(self):
        fonts = [
            {"name": "Rawline_Bold", "fn_regular": "./assets/rawline-700.ttf"},
        ]
        for font in fonts:
            LabelBase.register(**font)

if __name__ == '__main__':
    MainApp().run()