from kivy import platform

from kivy.uix.screenmanager import Screen

from screens import cam, file_picker


class Base(Screen):
    def __init__(self):
        super().__init__()
        self.cam = cam.Cam()
        self.file_picker = file_picker.FilePicker()

    def on_enter(self, *args):
        super().on_enter(*args)

        self.ids.item1.add_widget(self.cam)
        self.ids.item2.add_widget(self.file_picker)

        if platform == "android":
            from android.permissions import (
                request_permissions,
                Permission,
            )

            request_permissions(
                [
                    Permission.CAMERA,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.WRITE_EXTERNAL_STORAGE,
                ]
            )

        if platform == "win":
            self.cam.show_camera()
            self.file_picker.show_file_picker()
