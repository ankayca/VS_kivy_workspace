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
# local image builder
from kivy.lang import Builder
# internet image builder
from kivy.uix.image import AsyncImage
# defining the App class
class MyLabelApp(App):
    def build(self):
        screen = Screen()
        # label display the text on screen
        lbl = Label(text ="Label is Added on screen !!:):)")
        # Image builder from memory
        l=Builder.load_string("""Image:
        source: "220px-TaleUnknownIsland.jpg"
        pos_hint:{'center_x':0.14,'center_y':0.7}
        """)
        # Image builder from internet
        l1=AsyncImage(source= "https://1.bp.blogspot.com/-CwVfB-TrDh8/YVWuzVVwu4I/AAAAAAAACGo/4wnEXR4SQEcagqJEMTPTg0IEokAozmRswCLcBGAsYHQ/s346/220px-TaleUnknownIsland.jpg",
        pos_hint={'center_x':0.86,
                  'center_y':0.7})
        # text label
        l2 = Label(text ="Tale Unknown Island \n is amazing!!!", font_size ='37sp',pos_hint={'center_x':0.22,
                                                'center_y':0.35},color =[0.5, 0,1, 1])
        
        screen.add_widget(l)
        screen.add_widget(l1)
        screen.add_widget(l2)
        return screen

# creating the object
label = MyLabelApp()
# run the window
label.run()