import os
import winsound
from tkinter import filedialog




songDict = {}
accountFile = 'C:\\Users\\dunsi\\OneDrive\\Desktop\Soupify\\Accounts\\'
songFile = 'C:\\Users\\dunsi\\OneDrive\\Desktop\\Soupify\\Music\\'
savedUserFile = None

def loadSongs(username):#returns a dictionary of every song
    global songDict 
    with open (username+".txt","r") as spotifyDataFile:
        for i, song in enumerate(spotifyDataFile):

            print(i)
    return songDict

def playSong(songFileName):
    winsound.PlaySound(songFileName)

def playFrozen():
    winsound.PlaySound('Frozen.wav',winsound.SND_ASYNC)

def addSongs(songName, SongFile):
    global savedUserFile
    file = open(savedUserFile)
    file.write(songName+","+SongFile)
    file.close

def login(username, password):
    
    global savedUserFile
    print(accountFile.__dir__)
    if(not os.path.exists(accountFile+username+'.txt')):
        
        with open(accountFile+username+'.txt','a') as file:
            file.write("password: "+password)
            # if password = fir=st line then upload the songs and open the account else return bad somehow :)
        return 'you made a new account' 
        
    else:
        with  open(accountFile+ username+'.txt','a') as f:
            passwordString = 'password: '+password
            
        
        '''
        print (passwordString == f.readline())
        if( passwordString == f.readline()):
            savedUserFile = accountFile+ username+".txt"
            print('loading'+ savedUserFile)
            file.close()
            return 'you are logged into '+ username
        else:
            file.close()
            return 'wrong username or password :('
            '''
    return 'creation works'
