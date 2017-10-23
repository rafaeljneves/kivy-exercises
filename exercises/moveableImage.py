from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window


class character(Widget):
    pass


class MoveableImage(Image):

    def __init__(self, **kwargs):
        super(MoveableImage, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.x -= 10
        elif keycode[1] == 'right':
            self.x += 10
        elif keycode[1] == 'up':
            self.y += 10
        elif keycode[1] == 'down':
            self.y -= 10

        else:
            return False
        return True


class gameApp(App):
    def build(self):
        wimg = MoveableImage(source='../static/images/player1_r.png')
        m = character()
        m.add_widget(wimg)
        return m


if __name__ == '__main__':
    gameApp().run()
