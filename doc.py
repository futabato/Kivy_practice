from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class MyClass(objsct):
    def __init__(self):
        super(MyClass, self).__init__()
        self.numeric_var = 1
        
class MyClass(EventDispatcher):
    numeric_var = NumericProperty(1)
    
"""
<loginScreen>:
    f_username: username
    f_password: password
    GridLayout:
        rows: 2
        cols: 2
        padding: 10
        spacing: 10
        Label:
            text: 'User Name:'
        TextInput:
            id: username
        label:
            text: 'Password:'
        TextInput:
            id: password
            password: True
            
            
def on_touch_down(self, touch):
    if super(OurClassName, self).on_touch_down(touch):
        return True
    if not self.collide_point(touch.x, touch.y):
        return False
    print('you touched me!')
    return True
"""

