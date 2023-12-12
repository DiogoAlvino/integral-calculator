from kivymd.uix.screen import MDScreen
from processCalc import ProcessCalc
from kivy.uix.screenmanager import NoTransition, ScreenManager

class InputScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager(transition=NoTransition())

    def verify_calc(self):
        input_text = self.ids.input_calc.text
        if input_text:
            return ProcessCalc(integral_calc=input_text)