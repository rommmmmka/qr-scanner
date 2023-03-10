import os

from PIL import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from pyzbar import pyzbar


class FileLoader(Screen):
    Builder.load_file("layouts/file_loader.kv")

    def get_result(self, path, file):
        try:
            with Image.open(os.path.join(path, file[0])) as image:
                results = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.QRCODE])
                results = [str(result.data.decode("UTF-8")) for result in results]
                results = "\n".join(results)

                self.manager.get_screen("results").text = results
                self.manager.current = "results"
        except Exception:
            return
