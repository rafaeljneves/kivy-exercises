from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

builder_string = '''
RelativeLayout:
    padding: 10
    Button:
        text: '<<'
        size_hint: None, None
        size: 50,50 
        pos:  0, 0
    Button:
        text: '>>'
        size_hint: None, None
        size: 50,50
        pos:  100,0
'''

class controller(RelativeLayout):
    def __init__(self, **kwargs):
        super(controller, self).__init__(**kwargs)

        runTouchApp(Builder.load_string(builder_string))

class controllerApp(App):
    def build(self):
        return controller()

if __name__ == '__main__':
    controllerApp().run()
