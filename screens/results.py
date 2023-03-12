import webbrowser

import validators
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen


class Results(Screen):
    Builder.load_file("templates/layouts/results.kv")

    text = StringProperty()
    is_link = BooleanProperty()

    def on_enter(self):
        self.is_link = validators.url(self.text)

        action_btn = self.ids["action_btn"]
        if self.text:
            action_btn.text = (
                "Перайсці па спасылцы" if self.is_link else "Скапіраваць тэкст"
            )
            action_btn.size = 0, 0
            action_btn.size_hint = 1, 1
        else:
            self.text = "Памылка! QR-код не быў распазнаны"
            action_btn.size_hint = 0, 0

    def action(self):
        if self.is_link:
            webbrowser.open(self.text)
        else:
            Clipboard.copy(self.text)
