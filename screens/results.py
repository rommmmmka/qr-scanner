import webbrowser

import validators
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen


class Results(Screen):
    Builder.load_file("layouts/results.kv")

    text = StringProperty()
    is_link = BooleanProperty()

    def on_enter(self):
        self.is_link = validators.url(self.text)
        action_btn = self.ids["action_btn"]
        action_btn.text = "Перейти по ссылке" if self.is_link else "Скопировать текст"
        action_btn.size = 0, 0
        if not self.text:
            action_btn.size_hint = 0, 0
            self.text = "Ошибка! Текст не распознан"
        else:
            action_btn.size_hint = 1, 1

    def action(self):
        if self.is_link:
            webbrowser.open(self.text)
        else:
            Clipboard.copy(self.text)
