from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


kv = """
RelativeLayout:        
    padding: 10
    Image:            
        source: '../static/images/isometric_house.png'
        size: 50,50 #self.texture_size
        height: 400

    Image:
        source: '../static/images/player1_r.png'
        size: self.texture_size
        pos: 0,0   

    Label:
        text: 'Enjoy it! '            
        pos: 0,-200

    StackLayout:
        orientation: 'lr-tb'
        padding: 10
        spacing: 10
        Label:
            text: '           '
            font_size: 24
            bold: True
            color: (50,155,220,1)            
            size_hint: .2,.1

        Label:            
            text: '<><><><><>'
            pos: 300,500
            font_size: 24
            bold: True
            color: (1,255,255,1)            
            size_hint: .2,.1
        Label:
            text: 'Level: '
            font_size: 24
            bold: True
            color: (50,155,220,1)            
            size_hint: .2,.1
        
        Label:
            text: 'Score: '
            font_size: 24
            bold: True
            color: (50,155,220,1)            
            size_hint: .2,.1

"""


class controller(Widget):
    def __init__(self, **kwargs):
        super(controller, self).__init__(**kwargs)

        runTouchApp(Builder.load_string(kv))

class controllerApp(App):
    def build(self):

        parent = Widget()
        game = controller()
        btn_game = Button(text='Play')
        parent.add_widget(game)
        parent.add_widget(btn_game)

        return parent
        #return controller()

if __name__ == '__main__':
    controllerApp().run()
