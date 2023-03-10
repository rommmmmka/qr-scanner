from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import RiseInTransition, ScreenManager

from screens.cam import Cam
from screens.file_loader import FileLoader
from screens.results import Results


class QrScannerApp(App):
    def build(self):
        Window.size = 640, 530

        sm = ScreenManager(transition=RiseInTransition())
        cam = Cam(name="cam")
        results = Results(name="results")
        file_loader = FileLoader(name="file_loader")

        sm.add_widget(cam)
        sm.add_widget(results)
        sm.add_widget(file_loader)

        return sm


if __name__ == "__main__":
    QrScannerApp().run()
