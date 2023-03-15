from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import RiseInTransition, ScreenManager
from kivy import platform

from screens.base import Base

Builder.load_file("resources/templates/file_icon_entry.kv")
Builder.load_file("resources/templates/base.kv")
Builder.load_file("resources/templates/cam.kv")
Builder.load_file("resources/templates/file_picker.kv")


class QrScannerApp(MDApp):
    def build(self):
        if platform == "win":
            Window.size = 640, 530

        screen_manager = ScreenManager(transition=RiseInTransition())
        screen_manager.add_widget(Base())

        return screen_manager


if __name__ == "__main__":
    QrScannerApp().run()
