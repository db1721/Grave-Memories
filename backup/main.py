from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from Backend.numbers import generate_random_number


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = generate_random_number()
class memories(App):
    def build(self):
        """

        :return:
        """
        label = Label(text='Hello World')
        return MyRoot()


app = memories()
app.run()
