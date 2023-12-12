
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivy.uix.screenmanager import NoTransition, ScreenManager
from kivy.uix.image import Image
from scripts.formatLatex import latex_to_png
import os

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

            image_path = latex_to_png(self.integral_result, "result.png")
            image_widget = Image(source=image_path, nocache=True)
            results_container.add_widget(image_widget)
            
            app.root.current = "results"

    def go_to_input(self):
        previous_image = "result.png"
        if os.path.exists(previous_image):
            os.remove(previous_image)

        app = App.get_running_app()
        app.root.current = "input"