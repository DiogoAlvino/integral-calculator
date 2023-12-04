from scripts.calculator import calculator
from kivy.core.window import Window
from kivy.uix.screenmanager import NoTransition, ScreenManager
from kivymd.uix.screen import MDScreen
from results import ResultScreen

Window.size = (350, 600)

class ProcessCalc(MDScreen):
    def __init__(self, integral_calc=None, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = ScreenManager(transition=NoTransition())
        self.result_calc = calculator(integral_calc)
        if self.result_calc:
            self.callResults()

    def callResults(self):
        return ResultScreen(integral_result=self.result_calc['result'])
    
