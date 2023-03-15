from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Cam(Screen):
    Builder.load_file("templates/layouts/cam.kv")

    def get_result(self, symbols):
        if not symbols:
            return

        text = "\n".join([str(result.data.decode("UTF-8")) for result in symbols])

        self.manager.get_screen("results").text = text
        self.manager.current = "results"
