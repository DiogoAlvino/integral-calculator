
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import NoTransition, ScreenManager

class ResultScreen(MDScreen):
    def __init__(self, integral_result = None, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager(transition=NoTransition())
        self.integral_result = integral_result
        self.display_results()

    def display_results(self):
        if self.integral_result:
            app = App.get_running_app()
            results_screen = app.root.get_screen("results")
            results_container = results_screen.ids["results_container"]

            results_container.clear_widgets()

            label = MDLabel(text=f"RESULTADO: {self.integral_result}")
            label.id = "resultado"
            results_container.add_widget(label, 3)
            
            app.root.current = "results"

    def go_to_input(self):
        app = App.get_running_app()
        app.root.current = "input"