import winsound
musicLibrary = {'Frozen':'videoplayback.wav'} #this might work

def addSong(songName, fileName):# this might work
    musicLibrary[songName] = fileName
def removeSong(songName): #this might work
    def search(val,list):
        index = 0
        for x in list:
            if(x== val):
                val = x
                index += 1
                break
        return index
    removeIndex = search(songName,musicLibrary)

    del(musicLibrary[removeIndex])


def playSong(songName): #this works
    winsound.PlaySound(str(songName),winsound.SND_FILENAME |winsound.SND_ASYNC)
def playFrozen():
    playSong('Frozen.wav')
