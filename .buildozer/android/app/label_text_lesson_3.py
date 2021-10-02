from typing import Text
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
class Demo(MDApp):
 
    def build(self):
        #defining screen
        screen = Screen()

        #defining Image from memory label
        l=Builder.load_string("""Image:
            source: "220px-TaleUnknownIsland.jpg"
            pos_hint:{'center_x':0.14,'center_y':0.7}
            """)

        l1=AsyncImage(source= "https://1.bp.blogspot.com/-CwVfB-TrDh8/YVWuzVVwu4I/AAAAAAAACGo/4wnEXR4SQEcagqJEMTPTg0IEokAozmRswCLcBGAsYHQ/s346/220px-TaleUnknownIsland.jpg",
        pos_hint={'center_x':0.8,
                  'center_y':0.7})


        #defining 2nd label
        l2 = MDLabel(text="TaleUnknownIsland", pos_hint={'center_x':0.5,
                                                'center_y':0.4},
                     theme_text_color="Custom",
                     text_color=(0.5, 0, 0.5, 1),
                     font_style='H6')
         
        #defining 3rd label
        l3 = MDLabel(text="TaleUnknownIsland", pos_hint={'center_x':0.5,
                                                'center_y':0.35},
                     theme_text_color="Custom",
                     text_color=(0.5, 0,1, 1),
                      font_style='H4')
         
        screen.add_widget(l)
 
 
        screen.add_widget(l1)
        screen.add_widget(l2)
        screen.add_widget(l3)
        return screen
 
if __name__ == "__main__":
    Demo().run()