from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# 画面上の見た目や機能を構成するクラス
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        btn = Button(text="hello")
        self.add_widget(btn)
        
        btn2 = Button(text="exeryone")
        self.add_widget(btn2)
        
        #BoxLayoutというWidget
        b1 = BoxLayout()
        b1.orientation = "vertical"
        
        #b1に3つのボタンを追加
        btn3 = Button(text="how")
        btn4 = Button(text="are")
        btn5 = Button(text="you")
        
        #b1にボタンを追加
        b1.add_widget(btn3)
        b1.add_widget(btn4)
        b1.add_widget(btn5)
        
        #MainScreenにb1を追加
        self.add_widget(b1)
        
        btn6 = Button(text="today?")
        self.add_widget(btn6)
        

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