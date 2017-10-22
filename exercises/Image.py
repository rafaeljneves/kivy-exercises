from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder



runTouchApp(Builder.load_string('''
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
            color: (50,155,220,1)            
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



'''))