from kivy.app import App

from kivy.uix.image import Image





class MainApp(App):
    def build(self):
        img = Image(source='D:\projeler\sf_projeler\python_gui\Kivy\VS_kivy_workspace\\220px-TaleUnknownIsland.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()