from kivy.app import App
from kivy.uix.widget import Widget

class ClickInput(Widget):
    def on_touch_move(self, touch):
        print(touch)
        
class IntroKivy(App):
    def build(self):
        return ClickInput()
    
if __name__ == "__main__":
    IntroKivy().run()