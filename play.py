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
from kivy.animation import Animation
from kivy.graphics import Line, Color, Rectangle
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.image import Image
import socket, time, math, random, math
from random import randint
from kivy.clock import Clock
from kivy.vector import Vector

#Load kv file
Builder.load_file('settings.kv')

# Simple Kivy app



class WelcomeScreen(Screen):

    label_wid = ObjectProperty()


    def do_action(self):

        self.label_wid.text = 'Carregando...'

class character(Widget):
    pass


class BasicInstructions(Screen):
    pass




class PlayGame(Widget):

    pos_down = Vector(0, 0)
    pos_up = Vector(0, 0)
    points = NumericProperty(0)

    def __init__(self, **kwargs):
        print("Game Started OK...")
        super(PlayGame, self).__init__(**kwargs)
        randX = random.choice([0.1, 0.2, 0.8, 0.9])

        #self.enemy = self.drawEnemy(randX)
        #Clock.schedule_interval(self.enemy.drawWalking, 1)

        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            print("left: ",self.x)
            self.x -= 10
        elif keycode[1] == 'right':
            print("right: ", self.x)
            self.x += 10
        else:
            return False
        return True

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 0, 0)
            self.line = Line(points=(touch.x, touch.y, touch.x, touch.y), width=2)

    def on_mouse_move(self, mouse):
        with self.canvas:
            Color(1, 0, 0)
            self.line = Line(points=(mouse.x, mouse.y, mouse.x, mouse.y), width=2)

            self.line.points = [mouse.x, mouse.y, self.pos_down.x, self.pos_down.y]

    def on_touch_up(self, touch):
        self.canvas.remove(self.line)
        self.vel = Vector(-(self.pos_up[0] - self.pos_down[0]) / 10, -(self.pos_up[1] - self.pos_down[1]) / 10)


        # Randomly generating an enemy
    # def drawEnemy(self, x_pos):
    #     tmpEnemy = Enemy()
    #     tmpEnemy.x = self.width * x_pos
    #
    #     # 1280 is the width of the screen
    #     if (tmpEnemy.x < 1280 / 2):
    #         self.enemy_on_left = True
    #     else:
    #         self.enemy_on_left = False
    #
    #     randPos = randint(10, 90)
    #     # 1200 is the width of the screen
    #     tmpEnemy.y = float(randPos) / 100 * 800
    #
    #     tmpEnemy.velocity_x = 0
    #     tmpEnemy.velocity_y = randint(3, 5)
    #     tmpEnemy.spawnT = time.time()
    #
    #     self.add_widget(tmpEnemy)
    #     return tmpEnemy


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = PlayGame()
        self.add_widget(self.game)
        #Clock.schedule_interval(self.game.update, 1.0 / 60.0)



class Rotate(FloatLayout):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(Rotate, self).__init__(**kwargs)
        anim = Animation(angle = 360, duration=2)
        anim += Animation(angle = 360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(BasicInstructions(name='basic'))
game_screen = GameScreen(name='game')
sm.add_widget(game_screen)


#rt = FloatLayout()
#rt.add_widget(Rotate())


class MainApp(App,Image):

    # def __init__(self, **kwargs):
    #     super(MainApp, self).__init__(**kwargs)
    #     self._keyboard = Window.request_keyboard(None, self)
    #     if not self._keyboard:
    #         return
    #     self._keyboard.bind(on_key_down=self.on_keyboard_down)



    label = None
    botao = None
    image = None
    opcao = None

    def build(self):

        self.title = "Play Game"

        lista_opcoes = ["welcome", "setup_gui", "button_exercise", "relative_layout_exercise",
                        "stack_layout_exercise"]
        opcao = lista_opcoes[0]

        if   opcao == lista_opcoes[0]:
            #return sm
            layout = FloatLayout() # BoxLayout(orientation='vertical')
            layout.add_widget(sm)
            #layout.add_widget(rt)
            return layout  #Rotate()

        elif opcao == lista_opcoes[1]:
            return self.setup_gui()

        elif opcao == lista_opcoes[2]:
            return button_exercise.controllerApp().run()

        elif opcao == lista_opcoes[3]:
            return relative_layout_exercise.controllerApp().run()

        elif opcao == lista_opcoes[4]:
            return stack_layout_exercise.controllerApp().run()

    def play_game(self):
        print('Game Started...')
        self.wimg = Image(source='static/images/player1_r.png')
        game_screen.add_widget(self.wimg)

        return PlayGame()

    def setup_gui(self):

        self.image = Loader.image('player1.png')
        self.label = Label(text='loading...\n')
        self.botao = Button(text='Play')

        layout = BoxLayout(orientation='vertical')
        #layout.add_widget(self.image)
        layout.add_widget(self.label)
        layout.add_widget(self.botao)

        return layout

MainApp().run()

