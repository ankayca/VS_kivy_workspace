# import kivy module
import kivy
from kivy.uix.screenmanager import Screen
 
# this restricts the kivy version i.e
# below this kivy version you cannot use the app or software
kivy.require("1.9.1")
 
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
 
# if you not import label and use it it through error
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
# defining the App class
class MyLabelApp(App):
    def build(self):
        screen = Screen()
        # label display the text on screen
        lbl = Label(text ="Label is Added on screen !!:):)")
        # change only line 19 else all will same.
        l=Builder.load_string("""Image:
        source: "220px-TaleUnknownIsland.jpg"
        pos_hint:{'center_x':0.14,'center_y':0.7}
        """)
        l1=AsyncImage(source= "https://1.bp.blogspot.com/-CwVfB-TrDh8/YVWuzVVwu4I/AAAAAAAACGo/4wnEXR4SQEcagqJEMTPTg0IEokAozmRswCLcBGAsYHQ/s346/220px-TaleUnknownIsland.jpg",
        pos_hint={'center_x':0.8,
                  'center_y':0.7})
        # text colour
        l2 = Label(text ="Label is Added on \n screen !!:):)and its Multi\nLine", font_size ='20sp',color =[0.41, 0.42, 0.74, 1])
        screen.add_widget(l)
        screen.add_widget(l1)
        screen.add_widget(l2)
        return screen

# creating the object
label = MyLabelApp()
# run the window
label.run()