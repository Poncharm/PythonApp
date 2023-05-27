from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Привет, Антон! Ты самый лучший!')

if __name__ == '__main__':
    MyApp().run()
