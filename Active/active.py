from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class kvfile(App):
    def build(self):
        return Widgets()
    
if __name__ == "__main__":
    kvfile().run()