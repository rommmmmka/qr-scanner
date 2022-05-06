import os
import webbrowser

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.screenmanager import RiseInTransition, Screen, ScreenManager
from PIL import Image
from pyzbar import pyzbar
import validators


class Cam(Screen):

    def get_result(self, text):
        if not text:
            return
        self.manager.get_screen('results').text = text
        self.manager.current = 'results'


class Results(Screen):
    text = StringProperty()
    is_link = BooleanProperty()

    def on_enter(self):
        self.is_link = validators.url(self.text)
        action_btn = self.ids['action_btn']
        action_btn.text = 'Перейти по ссылке' if self.is_link else 'Скопировать текст'
        action_btn.size = 0, 0
        if not self.text:
            action_btn.size_hint = 0, 0
            self.text = 'Ошибка! Текст не распознан'
        else:
            action_btn.size_hint = 1, 1

    def action(self):
        if self.is_link:
            webbrowser.open(self.text)
        else:
            Clipboard.copy(self.text)


class FileLoader(Screen):

    def get_result(self, path, file):
        image = Image.open(os.path.join(path, file[0]))
        results = pyzbar.decode(image)
        self.manager.get_screen('results').text = ', '.join([str(symbol.data.decode('UTF-8')) for symbol in results])
        self.manager.current = 'results'


class QrScannerApp(App):

    def build(self):
        Window.size = 640, 530
        self.sm = ScreenManager(transition=RiseInTransition())
        self.cam = Cam(name='cam')
        self.results = Results(name='results')
        self.file_loader = FileLoader(name='file_loader')
        self.sm.add_widget(self.cam)
        self.sm.add_widget(self.results)
        self.sm.add_widget(self.file_loader)
        return self.sm


if __name__ == '__main__':
    QrScannerApp().run()
