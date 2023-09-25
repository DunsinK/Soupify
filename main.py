

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
import SpotifyLogic as Sl
from kivy.properties import ObjectProperty



class SpotifyGrid(Widget):
    name = ObjectProperty(None)
    password = ObjectProperty(None)
    def btn(self):
            #print("name: "+ self.name.text + "password: "+ self.password.text)
            with open('SpotifyData.txt', 'a+') as f:
                f.write("user: " + self.name.text +"\n pssw" + self.password.text+"\n")

            self.name.text = ""; self.password.text = ""
   
            
    



class SpotifyApp(App):
    def build(self):
        return SpotifyGrid()


if __name__ == '__main__':
    SpotifyApp().run()

''' <SpotifyGrid>

    name: name 
    email: email
    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2
            
            Label:
                text: "Name: "
            
            TextInput:
                id: name
                multiline: False

            Label: 
                text: "Email: "

            TextInput:
                id: email
                multiline:False
        Button:
            text: "Submit"
            on_press: root.btn()
            

        '''
