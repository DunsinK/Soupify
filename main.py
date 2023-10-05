

#kivy uix holds user interface elements
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import SoupifyLogic as Sl
from kivy.properties import ObjectProperty
import winsound
from tkinter import filedialog
from kivy.config import Config


class Song():
    def __init__(self,name,fileLocation):
        pass

    

class SpotifyGrid(Widget): ## root widget
    name = ObjectProperty(None)
    password = ObjectProperty(None)
    def btn(self):
            #print("name: "+ self.name.text + "password: "+ self.password.text)
            with open('SpotifyData.txt', 'a+') as f:
                f.write("user: " + self.name.text +"\n pssw" + self.password.text+"\n")

            self.name.text = ""; self.password.text = ""
   
            
    
class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def login(self):
        print(self.username.text)
        print(self.password.text)
        Sl.login(username= self.username.text, password= self.password.text)
class MainScreen(Screen):
    pass
class AddSongs(Screen):
    songname = ObjectProperty(None)
    songfile = ObjectProperty(None)
    def addSong(self):
        try: 
            if(os.path.isfile(self.songfile)):
                Sl.addSongs(self.songname.text,self.songfile.text)
            else:
                print("it didn't work")
                
            
        except:
            layout=GridLayout(cols = 1, padding = 10)

            popupLabel = Label(text = "Something went wront")
            closeButton = Button(text = "close", background_color = [1,0,0,1])

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            popup = Popup(title = 'notification Popup!', content = layout, size_hint = (None,None), size = (200,200))
            popup.open()

            closeButton.bind(on_press = popup.dismiss)


    def openFileExplorer(self):
        print('this is working')
        songName = filedialog.askopenfilename()
        self.songfile.text = songName

class PlaySongs(Screen):
    def playFrozen(self):
        Sl.playFrozen()
        print("you tryed to play frozen")



class SpotifyApp(App): # builds the app
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name= "mainScreen"))
        sm.add_widget(AddSongs(name="addSongs"))
        sm.add_widget(PlaySongs(name = "playSongs"))

        return sm
    



if __name__ == '__main__': #runs the code
    SpotifyApp().run()


