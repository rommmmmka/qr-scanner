from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import RiseInTransition, ScreenManager
from kivy import platform

from screens.cam import Cam
from screens.file_loader import FileLoader
from screens.results import Results


class QrScannerApp(App):
    Builder.load_file("templates/widgets/file_icon_entry.kv")

    def build(self):
        if platform == "win":
            Window.size = 640, 530

        if platform == "android":
            from android.permissions import request_permissions, Permission

            request_permissions(
                [
                    Permission.CAMERA,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.WRITE_EXTERNAL_STORAGE,
                ]
            )

        screen_manager = ScreenManager(transition=RiseInTransition())
        cam = Cam(name="cam")
        results = Results(name="results")
        file_loader = FileLoader(name="file_loader")

        screen_manager.add_widget(cam)
        screen_manager.add_widget(results)
        screen_manager.add_widget(file_loader)

        return screen_manager


if __name__ == "__main__":
    QrScannerApp().run()
