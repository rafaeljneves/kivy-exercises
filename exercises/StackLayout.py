from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image


builder_string = '''
StackLayout:
    orientation: 'lr-tb'
    padding: 10
    spacing: 10
    Label:
        text: '<><><><><>'
        size_hint: .2,.1
    Label:
        text: 'Level: '
        size_hint: .2,.1        
    Label:
        text: 'Score: '
        size_hint: .2,.1
                        
    Image:
        source: 'static/images/player1.png'
        size: self.texture_size
        size_hint: None, None
        pos: 300,300
'''

class controller(StackLayout):
    def __init__(self, **kwargs):
        super(controller, self).__init__(**kwargs)

        runTouchApp(Builder.load_string(builder_string))

class controllerApp(App):
    def build(self):
        return controller()

if __name__ == '__main__':
    controllerApp().run()
