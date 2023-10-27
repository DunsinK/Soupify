import os
import winsound
import shutil
from tkinter import filedialog
import kivy
import kivy.uix.button as Button


accountFile = 'C:\\Users\\dunsi\\OneDrive\\Desktop\Soupify\\Accounts\\'
songFolder = 'C:\\Users\\dunsi\\OneDrive\\Desktop\\Soupify\\Music\\'
savedUserFile = None

def loadSongs():# should load songs after every time playsongs is called/entered 
    pass
    if(savedUserFile == None):
        print("get gud nub")
        
    pass
    # take username and file then get all songs
    listOfSongs = []
    userFileText = ''
   
    with open(savedUserFile) as file:
        userFileText = [line.rstrip() for line in file]
        
    for line in open(savedUserFile):
        listOfSongs += line
    print(listOfSongs)
    pass
    '''# make songs into buttons
    listOfSongButtons = []
    for song in listOfSongs:
        makeSongButton(song)
    def makeSongButton(songName, songImg):
        btn = Button(text="song")'''
    
    



def playSong(songFileName):
    winsound.PlaySound(songFileName)

def playFrozen():
    winsound.PlaySound(songFolder+'Frozen.wav',winsound.SND_ASYNC)

def addSongs(songName, originalSongFile):
    shutil.copy(originalSongFile,songFolder)
    inProgramSongFileName = originalSongFile.split('/')[-1]
    try:
        os.rename(songFolder+inProgramSongFileName,songFolder+songName+'.mp3')
    except:
        print('song already exists')
    
    
    with open(savedUserFile, 'a') as file:
        file.write('songname: '+songName+'\n')
        

def login(username, password):
    
    global savedUserFile
    #print(accountFile.__dir__)
    if(not os.path.exists(accountFile+username+'.txt')):
        
        with open(accountFile+username+'.txt','a') as file:
            file.write('password: '+password+'\n')
            # if password = fir=st line then upload the songs and open the account else return bad somehow :)
            #loadSongs(username)
            savedUserFile = accountFile+username+'.txt'
        return 'you made a new account' 
        
    else:
        givenPassword = None
        passwordString = None
        with open(accountFile+ username+'.txt','r') as file:
            passwordString = 'password: '+password+'\n'
            givenPassword = file.readline()
        
        #print(givenPassword  +" the real password is "+ passwordString)
        if(givenPassword == passwordString):
            #loadSongs(username)
            savedUserFile = accountFile+username+'.txt'
            return 'you are logged into '+username
        else:
            return 'wrong password or username was given'
            
    
