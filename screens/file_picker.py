import os
import webbrowser

from PIL import Image
from kivy import platform
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import Screen
from pyzbar import pyzbar

from misc.create_dialog import create_dialog


class FilePicker(Screen):
    def permissions_check(self):
        if platform == "android":
            from android.permissions import (
                check_permission,
                request_permissions,
                Permission,
            )

            if check_permission(
                "android.permission.READ_EXTERNAL_STORAGE"
            ) and check_permission("android.permission.WRITE_EXTERNAL_STORAGE"):
                self.show_file_picker()
            else:
                request_permissions(
                    [
                        Permission.READ_EXTERNAL_STORAGE,
                        Permission.WRITE_EXTERNAL_STORAGE,
                    ]
                )

        if platform == "win":
            self.show_file_picker()

    def show_file_picker(self):
        screen = self.ids.file_picker_screen
        screen.remove_widget(self.ids.files_no_access)
        screen.add_widget(FilePickerWidget())


class FilePickerWidget(Screen):
    def get_result(self, path, file):
        try:
            with Image.open(os.path.join(path, file[0])) as image:
                results = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.QRCODE])
                text = "\n".join(
                    [str(result.data.decode("UTF-8")) for result in results]
                )
        except:
            text = ""

        self.dialog = create_dialog(
            text,
            self.visit_link,
            self.copy_text,
            self.close_dialog,
            self.on_dismiss_dialog,
        )
        self.dialog.open()

    def visit_link(self, inst):
        webbrowser.open(self.dialog.text)

    def copy_text(self, inst):
        Clipboard.copy(self.dialog.text)

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def on_dismiss_dialog(self, inst):
        pass
