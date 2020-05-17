from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# `.py`ファイルには垣田kないので，Widgetsがどのようなクラスなのかも，後でまとめてkvファイルにかいてしまおう
class Widgets(Widget):
    pass

class kvfile(App):
    def build(self):
        return Widgets()
    
if __name__ == "__main__":
    kvfile().run()