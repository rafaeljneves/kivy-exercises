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
from exercises import button as button_exercise, RelativeLayout as relative_layout_exercise, StackLayout as stack_layout_exercise

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
    opcao = None

    def build(self):

        self.title = "Play Game"

        lista_opcoes = ["welcome", "setup_gui", "button_exercise", "relative_layout_exercise",
                        "stack_layout_exercise"]
        opcao = lista_opcoes[4]

        if   opcao == lista_opcoes[0]:
            return sm

        elif opcao == lista_opcoes[1]:
            return self.setup_gui()

        elif opcao == lista_opcoes[2]:
            return button_exercise.controllerApp().run()

        elif opcao == lista_opcoes[3]:
            return relative_layout_exercise.controllerApp().run()

        elif opcao == lista_opcoes[4]:
            return stack_layout_exercise.controllerApp().run()


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

