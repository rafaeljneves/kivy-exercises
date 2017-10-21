# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.loader import Loader
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

#Load kv file
Builder.load_file('settings.kv')

# Simple Kivy app

class WelcomeScreen(Screen):

    label_wid = ObjectProperty()


    def do_action(self):

        self.label_wid.text = 'Carregando...'



sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))

class MainApp(App):

    label = None
    botao = None
    image = None

    def build(self):
        #root = self.setup_gui()
        self.title = "Play Game"
        return sm

    def setup_gui(self):

        self.image = Loader.image('playerboy_big.png')
        self.label = Label(text='carregando...\n')
        self.botao = Button(text='Play')

        layout = BoxLayout(orientation='vertical')
        #layout.add_widget(self.image)
        layout.add_widget(self.label)
        layout.add_widget(self.botao)

        return layout

MainApp().run()
