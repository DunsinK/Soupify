import winsound

def loadSongs(username):#returns a dictionary of every song
    songDict = {}
    with open ("SpotifyData.txt","r") as spotifyDataFile:
        for song in spotifyDataFile:
            print(song)
    return songDict

def playSong(songFileName):
    winsound.PlaySound(songFileName)

def login():
    pass