from pages.base import BaseScreen
from kivy.core.window import Window


class PageLacak(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.back_click)

    def back_click(self, window, key, *largs):
        if key == 27:
            self.root.navigate_to("main_screen", None)
            return True


