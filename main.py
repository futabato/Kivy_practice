from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# 画面上の見た目や昨日を構成するクラス
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        btn = Button(text="hello")
        self.add_widget(btn)
        
        btn2 = Button(text="exeryone")
        self.add_widget(btn2)

# アプリを構成するクラス
class MainApp(App):
    def on_start(self):
        print("App Start!")
    
    def build(self):
        MS = MainScreen()
        return MS

    def on_stop(self):
        print("App End!")

if __name__=="__main__":
    MainApp().run()