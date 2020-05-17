# coding:utf-8

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello from t_o_d')

MyApp().run()