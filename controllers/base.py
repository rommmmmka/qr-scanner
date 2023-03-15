from kivy import platform

from kivy.uix.screenmanager import Screen


from controllers import cam, file_picker


class Base(Screen):
    def __init__(self):
        super().__init__()
        self.cam = cam.Cam()
        self.file_picker = file_picker.FilePicker()

    def on_enter(self, *args):
        super().on_enter(*args)

        if platform == "android":
            from android.permissions import request_permissions, Permission

            request_permissions([Permission.CAMERA], self.cam.permissions_callback)
            request_permissions(
                [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE],
                self.file_picker.permissions_callback,
            )

        if platform == "win":
            # self.cam.show_camera()
            self.file_picker.show_file_picker()

        self.ids.item1.add_widget(self.cam)
        self.ids.item2.add_widget(self.file_picker)
