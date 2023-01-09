from tkinter import *
from time import strftime
from bs4 import BeautifulSoup
import urllib.request, re, random, time, wget, ctypes
from time import strftime
import os

root = Tk()
root.title("Wallpaper generator")
root.resizable(False, False)

curTime = 600
tempFileName = ""
genre = "anime"
genres = ['anime', 'gaming', 'animal', 'fantasy', 'nature', 'music', 'space']
images = []
counter = 0
stopped = 1

minlist = [300, 600, 1800, 10]
def change_wallpaper():
    global tempFileName
    global images
    html_page = urllib.request.urlopen(f"https://wallpapers.com/{genre}")
    soup = BeautifulSoup(html_page, 'html.parser')
    for img in soup.findAll('source'):
        if 'webp' in img.get('srcset'):
            images.append(img.get('srcset'))
    rn = random.randint(0, len(images))
    wallpaper = f"https://wallpapers.com/{images[rn]}"
    filename = wget.download(wallpaper)
    tempFileName = filename
    path = f"C:\\Users\\liam\\Documents\\NewCodespace\\WebScrape\\{filename}"
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
    images = []

def time():
    global genre
    global counter
    global curTime
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
    current.config(text = f"{int(curTime / 60)} Minutes")
    currentGenre.config(text = f"Genre: {genre}")
    counter += 1
    if stopped == 0 and counter >= curTime:
        if os.path.exists(tempFileName):
            os.remove(tempFileName)
        change_wallpaper()
        counter = 0
        
def stop():
    global stopped
    stopped = 1

def start():
    global counter
    global stopped 
    counter = 0
    stopped = 0
    
def setTimer(n):
    global curTime
    curTime = minlist[n]

def setGenre(n):
    global genre
    genre = genres[n]
    
canvas = Canvas(root, height=420, width=600, bg="#262626")
canvas.pack()

playBut = PhotoImage(file="play.png")
play = Button(root, image=playBut, borderwidth=0, bg='#262626', command=start)
play.place(x=235, y=100)

pauseBut = PhotoImage(file="pause.png")
pause = Button(root, image=pauseBut, borderwidth=0, bg='#262626', command=stop)
pause.place(x=300, y=100)

header = Label(root, text="Wallpaper Generator", font="Helvetica 16 bold italic", bg="#262626", fg="#32DCFF")
header.place(x=20, y=13)

timerText = Label(root, text="Timer:", font="Helvetica 16 bold italic", bg="#262626", fg="#32DCFF")
timerText.place(x=350, y=13)

fiver = Button(root, text="5 Minutes", padx=1, pady=1, bg="gray", command= lambda n = 0: setTimer(n))
fiver.place(x=520, y=14)

tenner = Button(root, text="10 Minutes", padx=1, pady=1, bg="gray", command= lambda n = 1: setTimer(n))
tenner.place(x=520, y=50)

halfa = Button(root, text="30 Minutes", padx=1, pady=1, bg="gray", command= lambda n = 2: setTimer(n))
halfa.place(x=520, y=86)

tenSec = Button(root, text="10 seconds", padx=1, pady=1, bg="gray", command= lambda n = 3: setTimer(n))
tenSec.place(x=520, y=122)

mark = Label(root, font=('calibri', 40, 'bold'), pady=5, fg='black', bg="#262626")
mark.place(x=10, y=220)

current = Label(root, font=('calibri', 40, 'bold'), pady=5, fg='black', bg="#262626")
current.place(x=10, y=150)

currentGenre = Label(root, font=('calibri', 40, 'bold'), fg='black', bg="#262626")
currentGenre.place(x=10, y=335)

genreAnime = Button(root, text="Anime", padx=1, pady=1, bg="gray", command= lambda n = 0: setGenre(n))
genreAnime.place(x=10, y=310)

genreGaming = Button(root, text="Gaming", padx=1, pady=1, bg="gray", command= lambda n = 1: setGenre(n))
genreGaming.place(x=60, y=310)

genreAnimal = Button(root, text="Animals", padx=1, pady=1, bg="gray", command= lambda n = 2: setGenre(n))
genreAnimal.place(x=117, y=310)

genreFantasy = Button(root, text="Fantasy", padx=1, pady=1, bg="gray", command= lambda n = 3: setGenre(n))
genreFantasy.place(x=175, y=310)

genreNature = Button(root, text="Nature", padx=1, pady=1, bg="gray", command= lambda n = 4: setGenre(n))
genreNature.place(x=230, y=310)

genreMusic = Button(root, text="Music", padx=1, pady=1, bg="gray", command= lambda n = 5: setGenre(n))
genreMusic.place(x=282, y=310)

genreSpace = Button(root, text="Space", padx=1, pady=1, bg="gray", command= lambda n = 6: setGenre(n))
genreSpace.place(x=330, y=310)

pathDir = "C:\\Users\\liam\\Documents\\NewCodespace\\WebScrape"
for image in os.listdir(pathDir):
    if (image.endswith('.webp')):
        os.remove(image)

time()

root.mainloop()