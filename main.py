import webbrowser

import validators
from kivy.app import App
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
# from pyzbar.pyzbar import decode
# from kivy_garden.zbarcam import ZBarCam
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition


class Cam(Screen):

    def show_result(self, text):
        if not text:
            return
        self.manager.get_screen('results').text = text
        self.manager.current = 'results'


class Results(Screen):
    text = StringProperty()
    is_link = BooleanProperty()

    def on_enter(self):
        self.is_link = validators.url(self.text)
        self.ids['action_btn'].text = 'Перейти по ссылке' if self.is_link else 'Скопировать текст'

    def action(self):
        if self.is_link:
            webbrowser.open(self.text)
        else:
            Clipboard.copy(self.text)


class QrScannerApp(App):
    # Builder.load_file("qrscanner.kv")

    def build(self):
        self.sm = ScreenManager(transition=RiseInTransition())
        self.cam = Cam(name='cam')
        self.results = Results(name='results')
        self.sm.add_widget(self.cam)
        self.sm.add_widget(self.results)
        return self.sm


if __name__ == '__main__':
    QrScannerApp().run()
