

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
import SoupifyLogic as Sl
from kivy.properties import ObjectProperty
import winsound


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
    songName = ObjectProperty(None)
    songFile = ObjectProperty(None)
    def addSong(self):
        Sl.addSong(self.songName,self.songFile)
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


