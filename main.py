import random
import requests
from io import BytesIO

from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk,Image
from googleImageSearch import *
from readfile import *

root = Tk()
root.title('LearnWithGoogleImages')
root.iconbitmap('LWGI_icon.ico')

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

image_label = Label()
originalWord = Label()
translatedWord = Label()
wordnumber = 0

def newimage():
    global image_label
    global originalWord
    global translatedWord
    originalWord.grid_forget()
    translatedWord.grid_forget()
    image_label.grid_forget()
    getNewImage()

def showword():
    global wordnumber
    global originalWord
    originalWord = Label(root, text=wordList[wordnumber][0], font=fontStyle)
    originalWord.grid(row=2, column=1)

def showtranslation():
    global wordnumber
    global translatedWord
    translatedWord = Label(root, text=wordList[wordnumber][1], font=fontStyle)
    translatedWord.grid(row=2, column=2)

button_newimage = Button(root, text="New Image", command=newimage)
button_showword = Button(root, text="Show Word", command=showword)
button_showtranslation = Button(root, text="Show Translation", command=showtranslation)

button_newimage.grid(row=1, column=0)
button_showword.grid(row=1, column=1)
button_showtranslation.grid(row=1, column=2)

def getNewWordNumber():
    return random.randrange(0, len(wordList)-1)

def getNewImage():
    global wordnumber
    wordnumber = getNewWordNumber()
    word_to_search = wordList[wordnumber][0]
    print(word_to_search)
    results = google_search(word_to_search, my_api_key, my_cse_id, num=1)
    print(results[0]["link"])

    response = requests.get(results[0]["link"])

    baseheight = 400

    subject_img = Image.open(BytesIO(response.content))
    hpercent = (baseheight / float(subject_img.size[1]))
    wsize = int((float(subject_img.size[0]) * float(hpercent)))
    subject_img = subject_img.resize((wsize, baseheight), Image.ANTIALIAS)
    subject_img = ImageTk.PhotoImage(subject_img)

    global image_label
    image_label = Label(image=subject_img)
    image_label.image = subject_img
    image_label.grid(row=0, column=0, columnspan=3)

def main():
    readWordListFromFile()
    getNewImage()
    root.mainloop()

if __name__ == '__main__':
  main()
