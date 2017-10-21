from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class controller(BoxLayout):

    def __init__(self, **kwargs):
        super(controller,self).__init__(**kwargs)

        self.padding = 200

        button = Button(text='Button Exercise')
        self.add_widget(button)

class controllerApp(App):
    def build(self):
        return controller()

if __name__ == '__main__':
    controllerApp().run()
