from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# ユーザ名入力フォームのクラスを作成
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2                                   #LoginScreenのレイアウトを2列する
        self.add_widget(Label(text = "Username:"))
        self.username = TextInput(multiline = False)    #1行のみ書く時は`False`
        self.add_widget(self.username)

        # パスワードの入力欄を追加
        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)
class IntroKivy(App):
    def build(self):
        return LoginScreen()
    
if __name__ == "__main__":
    IntroKivy().run()