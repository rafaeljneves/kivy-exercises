from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

# config
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(1,1,0)
            d = 30.
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d))


class MyPaintApp(App):
    def builder(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
