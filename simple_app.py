import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import random as r
KV='''Button:
text:"CLICK HERE!"
size_hint:(.2,.2)
on_press:app.color()'''

class MyApp(App)
    def build(self):
        return Builder.load_string(KV)
    def color(self):
        self.root.pos_hint={
            'center_x':0.5,
            'center_y':0.5
        }
        Window.clearcolor = (
            r.uniform(0,1),r.uniform(0,1),
            r.uniform(0, 1), 1

        )
MyApp().run()
