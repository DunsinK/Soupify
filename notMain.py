import tkinter as tk
from tkinter import*
import winsound
import SongFunctions as sf
import kivy

window = Tk() #root
window.title('Soupify')
window.geometry('800x800')
frame = tk.Frame(window)


searchPanel = PanedWindow(master= window, bd = 4, bg = 'blue', orient=VERTICAL,relief='raised')
searchPanel.pack(fill = BOTH, expand = 1)
left = Label(searchPanel, text="this is a left thing")
searchPanel.add(left)

mainPanel =PanedWindow(master = searchPanel,relief='raised' ,bd= 4, bg='red')
searchPanel.add(mainPanel)

playPanel =PanedWindow(master = mainPanel, relief='raised',bd = 4, bg = 'green')
#mainPanel.add(playPanel)


playButton = tk.Button(master=window,text='Pavan Likes Frozen',command= lambda: sf.playFrozen()).pack()

songNameVar = tk.StringVar()
addSongnameEntry = tk.Entry(master=window, textvariable=songNameVar).pack()
addSongButton = tk.Button(master=window)

#placing things
#playButton.grid(row = 0,column= 1)


mainloop()


