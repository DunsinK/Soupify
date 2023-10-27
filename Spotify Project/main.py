

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


#creates screen manager
sm = ScreenManager()



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
    popup = Popup()


    def hide(self):
        self.password.password = not self.password.password == True
    
    def toMainScreen(self, a, b,popup):
                if a == 'you are logged into '+ b or a == 'you made a new account':
                    sm.current = 'mainScreen'
                return self.popup.dismiss

    def login(self):
        try:
            response = Sl.login(username= self.username.text, password= self.password.text) 
            
            layout=GridLayout(cols = 1, padding = 10)

            popupLabel = Label(text = response)
            closeButton = Button(text = "close", background_color = [1,0,0,1])

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            self.popup = Popup(title = 'notification Popup!', content = layout, size_hint = (None,None), size = (200,200))
            self.popup.open()

            closeButton.bind(on_press = self.toMainScreen(response,self.username.text,self.popup))

        except:
            layout=GridLayout(cols = 1, padding = 10)

            popupLabel = Label(text = "Something went wrong")
            closeButton = Button(text = "close", background_color = [1,0,0,1])

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            popup = Popup(title = 'notification Popup!', content = layout, size_hint = (None,None), size = (200,200))
            popup.open()

            closeButton.bind(on_press = popup.dismiss)

            
    
class MainScreen(Screen):
    def toPlaySongs(self):
        sm.current = 'playSongs'
        Sl.loadSongs()

class AddSongs(Screen):
    songname = ObjectProperty(None)
    songfile = ObjectProperty(None)

    def addSong(self):   
        
        if(os.path.isfile(self.songfile.text)):
            Sl.addSongs(self.songname.text,self.songfile.text)
            layout=GridLayout(cols = 1, padding = 10)

            popupLabel = Label(text = "Song Created")
            closeButton = Button(text = "close", background_color = [1,0,0,1])

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            popup = Popup(title = 'notification Popup!', content = layout, size_hint = (None,None), size = (200,200))
            popup.open()

            closeButton.bind(on_press = popup.dismiss)
        else:
            layout=GridLayout(cols = 1, padding = 10)

            popupLabel = Label(text = "Bad File")
            closeButton = Button(text = "close", background_color = [1,0,0,1])

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            popup = Popup(title = 'notification Popup!', content = layout, size_hint = (None,None), size = (200,200))
            popup.open()

            closeButton.bind(on_press = popup.dismiss)
        try:
                pass
        except:
            layout=GridLayout(cols = 1, padding = 10)

            popupLabel = Label(text = "Something went wronger")
            closeButton = Button(text = "close", background_color = [1,0,0,1])

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            popup = Popup(title = 'notification Popup!', content = layout, size_hint = (None,None), size = (200,200))
            popup.open()

            closeButton.bind(on_press = popup.dismiss)


    def openFileExplorer(self):
        songName = filedialog.askopenfilename()
        self.songfile.text = songName

class PlaySongs(Screen):
    def loadSongs(self):
        Sl.loadSongs()
    def playFrozen(self):
        Sl.playFrozen()
        print("you tryed to play frozen")


class SpotifyApp(App): # builds the app
    def build(self):
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name= "mainScreen"))
        sm.add_widget(AddSongs(name="addSongs"))
        sm.add_widget(PlaySongs(name = "playSongs")) 
        return sm
    


if __name__ == '__main__': #runs the code
    SpotifyApp().run()


