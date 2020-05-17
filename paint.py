from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class DrawInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            # `ud` = User data Dictionary
            touch.ud["Line"] = Line(points = (touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud["Line"].points += touch.x, touch.y
    def on_touch_up(self, touch):
        print(touch.ud["Line"].points)

class Introkivy(App):
    def build(self):
        return DrawInput()
    
if __name__ == "__main__":
    Introkivy().run()