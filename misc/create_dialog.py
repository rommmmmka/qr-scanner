import validators
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


def create_dialog(
    text, visit_link_f, copy_text_f, close_dialog_f, on_dismiss_dialog_f
) -> MDDialog:
    buttons = []
    if text:
        if validators.url(text):
            buttons.append(
                MDFlatButton(text="ПЕРАЙСЦІ ПА СПАСЫЛЦЫ", on_release=visit_link_f)
            )
        else:
            buttons.append(
                MDFlatButton(text="СКАПІРАВАЦЬ ТЭКСТ", on_release=copy_text_f)
            )
    else:
        text = "Памылка! QR-код не быў распазнаны"

    buttons.append(
        MDFlatButton(text="ОК", on_release=close_dialog_f),
    )

    return MDDialog(text=text, buttons=buttons, on_dismiss=on_dismiss_dialog_f)
