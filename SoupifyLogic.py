import os
import winsound
from tkinter import filedialog




savedUserFile = None

def loadSongs(username):#returns a dictionary of every song
    songDict = {}
    with open ("SpotifyData.txt","r") as spotifyDataFile:
        for song in spotifyDataFile:
            print(song)
    return songDict

def playSong(songFileName):
    winsound.PlaySound(songFileName)

def playFrozen():
    winsound.PlaySound('Frozen.wav',winsound.SND_ASYNC)

def addSongs(songName, SongFile):
    pass

def login(username, password):
    global savedUserFile
    if(not os.path.exists(username+".txt")):
        
        f = open(username+".txt","x")
        f.write("password: "+password)
        # if password = first line then upload the songs and open the account else return bad somehow :)
        print(f.read)
        f.close
        loadSongs()
    else:
        f = open(username+'.txt','r+')
        passwordString = 'password: '+password
        f.readline
        if( passwordString == f.readline()):
            savedUserFile = username+".txt"