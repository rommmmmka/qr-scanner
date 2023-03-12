from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Cam(Screen):
    Builder.load_file("templates/layouts/cam.kv")

    def get_result(self, text):
        if not text:
            return

        self.manager.get_screen("results").text = text
        self.manager.current = "results"
