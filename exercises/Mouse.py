import kivy
kivy.require('1.10.0')

from kivy.core.window import Window
from kivy.app import App
from kivy.clock import Clock
from functools import partial


class MyMouse(App):

    def __init__(self, **kwargs):
        super(MyMouse, self).__init__(**kwargs)
        Clock.schedule_interval(partial(self.my_callback), 0.05)

    def my_callback(self, dt):
        print(Window.mouse_pos)

if __name__ == '__main__':
    MyMouse().run()