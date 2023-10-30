import pygame
from  tkinter import *
from tkinter import filedialog

pygame.init()
win = Tk()
win.title("Music Player")
win.geometry("900x500")
win.config(bg='sky blue')



def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Control functions
def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()



f1 = ("arial",20,"bold")

load_bt=Button(win,text="Select song",font=f1,command=load_music,bg='light goldenrod',fg='black')
load_bt.place(x=362,y=400)

play_bt=Button(win,text="Play",font=f1,command=play_music,bg='black',fg='white')
play_bt.place(x=252,y=200)

pause_bt=Button(win,text="Pause",font=f1,command=pause_music,bg='black',fg='white')
pause_bt.place(x=402,y=200)

stop_bt=Button(win,text="Stop",font=f1,command=stop_music,bg='black',fg='White')
stop_bt.place(x=562,y=200)



win.mainloop()