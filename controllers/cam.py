import webbrowser

from kivy import platform
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import Screen

from misc.create_dialog import create_dialog


class Cam(Screen):
    def permissions_callback(self, _permissions, grant_results):
        if all(grant_results):
            self.show_camera()

    def permissions_check(self):
        if platform == "android":
            from android.permissions import (
                check_permission,
                request_permissions,
                Permission,
            )

            if check_permission("android.permission.CAMERA"):
                self.show_camera()
            else:
                request_permissions([Permission.CAMERA], self.permissions_callback)

        if platform == "win":
            self.show_camera()

    def show_camera(self):
        screen = self.ids.camera_screen
        screen.remove_widget(self.ids.camera_no_access)
        cam_widget = CamWidget()
        screen.add_widget(cam_widget)


class CamWidget(Screen):
    def __init__(self):
        super().__init__()
        self.dialog = None
        self.dialog_state = False

    def get_result(self, symbols):
        if not symbols:
            return

        text = "\n".join([str(result.data.decode("UTF-8")) for result in symbols])

        if not self.dialog_state:
            self.dialog = create_dialog(
                text,
                self.visit_link,
                self.copy_text,
                self.close_dialog,
                self.on_dismiss_dialog,
            )
            self.dialog.open()
            self.dialog_state = True

    def visit_link(self, inst):
        webbrowser.open(self.dialog.text)

    def copy_text(self, inst):
        Clipboard.copy(self.dialog.text)

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def on_dismiss_dialog(self, inst):
        self.dialog_state = False
