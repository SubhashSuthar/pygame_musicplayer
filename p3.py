
#complete music player
from datetime import date


print("")
print("Windows Sound Manager (Python 2)")
print("Copyright (c) 2014 - %d | Paradoxis" % date.today().year)
print("")


import pygame
pygame.init()

#drum = pygame.mixer.Sound("Radio.mp3")
#cymbal = pygame.mixer.Sound("TumSaathHo.mp3")

#drum.play()

#pygame music player
#tkinter GUI
#mutagen to handle audio metadata

import os
from Tkinter import *
from tkinter.filedialog import askdirectory

channel1 = Tk()

while True:
    print(pygame.mixer.music.get_volume())
    break

channel1.minsize(300,300)

listofsongs = []
realnames = []

index = 0

def nextsong(self):
    global index
    index+=1
    if (index==len(listofsongs)):
        index = 0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def previoussong(self):
    global index
    index-=1
    if (index==-1):
        index = len(listofsongs)-1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopsong(self):
    pygame.mixer.music.stop()

def pausesong(self):
    pygame.mixer.music.pause()

def playsong(self):
    pygame.mixer.music.unpause()

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            
            #audio = ID3(realdir)
            #realnames.append(audio[TIT2].text[0])
            realnames.append(file)
            listofsongs.append(file)
            print(file)
 
    print(listofsongs)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

label = Label(channel1,text='music player')
label.pack()

listbox = Listbox(channel1)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()
for i in realnames:
    listbox.insert(0,i)

#defining music controls
nextbutton = Button(channel1,text='next Button')
nextbutton.pack()

previousbutton = Button(channel1,text='previous Button')
previousbutton.pack()

stopbutton = Button(channel1,text='stop Button')
stopbutton.pack()

playbutton = Button(channel1,text='play Button')
playbutton.pack()

pausebutton = Button(channel1,text='pause Button')
pausebutton.pack()

def updateVolume(event):
    
    a = int(event)
    b = (a/100.00)
    pygame.mixer.music.set_volume(b)
    print("music volume: ",pygame.mixer.music.get_volume())
    print("slider value: ", event)

w = Scale(channel1, from_=0, to=100, resolution=1, orient=HORIZONTAL, command=updateVolume)
w.pack()
print(w)

#python events binding with button click
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",playsong)
pausebutton.bind("<Button-1>",pausesong)

#python event binding with clicking on listbox
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()




listbox.bind('<<ListboxSelect>>', onselect)


channel1.mainloop()