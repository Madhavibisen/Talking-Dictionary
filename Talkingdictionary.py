#Refer 1. pexel.com for bg images   2. icon-icons.com  for small images  3. flayicons.com
from tkinter import *
from tkinter import messagebox
import json
import pyttsx3
from difflib import get_close_matches

engine=pyttsx3.init()
voices = engine.getProperty('voices')                             #getting details of current voice
#engine.setProperty('voice', voices[0].id)                        #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)                         #changing index, changes voices. 1 for female

rate=engine.getProperty('rate')
engine.setProperty('rate',200)                                    #by default rate is 200

#get_close_matches(appel,['ape','apple','apes','peach','fan'],n=3,cutoff=0.6) #0.0 to 1.0
#print(word)

def wordaudio():
    engine.say(enterwordentry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()


def iexit():
    res=messagebox.askyesno('confirm','Do you want to exit?')
    if res==True:
        root.destroy()                                              #If we will click on yes it will destroy the window.
    else:
        pass                                                        #Nothing will happen if we click on No.

def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0,END)                                    #It will clear the area where we are writing the word for which we want meaning.
    textarea.delete(1.0,END)                                        #It will clear the area where meaning is getting printed.
    textarea.config(state=DISABLED)

def search():
    data=json.load(open('data.json'))                               #Data will get loaded in variable data.
    word=enterwordentry.get()                                       #Here whatever we are goig to search will get stored in variable word.
    word=word.lower()                                               #It will convert words in lowercase.

    if word in data:
        meaning=data[word]                                          #Meaning will get fetch for the word in meaning variable.
        textarea.config(state=NORMAL)
        textarea.delete(1.0,END)                                    #It will remove Previous data from the meaning text area.
        for item in meaning:                                        #as there are more than one meanings are available for one word,we are getting meanings in unstructured manner like paranthesis are present and each menaing should be in new line.
            textarea.insert(END,u'\u2022'+item+'\n\n')              #here \u2022 is the code for bullets and \n for next line.
        textarea.config(state=DISABLED)
            #textarea.insert(END,data[word])

    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        #print(close_match)
        res=messagebox.askyesno('Confirm','did you mean ' +close_match+  ' instead?')

        if res==True:
            meaning=data[close_match]
            textarea.delete(1.0, END)
            textarea.config(state=NORMAL)

            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')
                textarea.config(state=DISABLED)

        else:
            textarea.delete(1.0,END)
            messagebox.showinfo('Information','The word doesnt exist, Please type a correct word.')
            enterwordentry.delete(0,END)

    else:
        messagebox.showerror('Error','The word doesnt Exist.Please double check it')
        enterwordentry.delete(0,END)



#GUI
root=Tk()                                                          #A window will get created.
root.geometry('1000x626+100+50')                                   #To fix the position of window.
root.title('Talking Dictionary Created by Madhavi Bisen')          #It will give title to the window.
root.resizable(0,0)                                                #It will disable the maximize button.

bgImage=PhotoImage(file='bg1.png')                                  #Background image.
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)                                             #Position of background image on the window.

enterwordLabel = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3',bg='whitesmoke')  #It will create label as 'Enter Word'.
enterwordLabel.place(x=530, y=20)                                                                           #Position of label will be set.

enterwordentry = Entry(root, font=('arial', 23, 'bold'),bd=8,relief=GROOVE,justify=CENTER)                  #bd=border, relief=border style, justify=text position in entry box
enterwordentry.place(x=510, y=80)                                                                           #Position of Entry box.

enterwordentry.focus_set()                                         #It will blink the cursor as we will run the program.

searchimage = PhotoImage(file='search.png')
searchbutton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=search)  #Search button with image.
searchbutton.place(x=620, y=150)

micimage = PhotoImage(file='mic.png')
micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=wordaudio)        #mic button with image.
micButton.place(x=710, y=153)

meaninglabel = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')                #It will create Label as 'Meaning'
meaninglabel.place(x=580, y=240)

textarea = Text(root, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')               #It will create text field, wrap=it will move whole word to the next line.
textarea.place(x=460, y=300)

microimage = PhotoImage(file='microphone.png')
microbutton = Button(root, image=microimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=meaningaudio)
microbutton.place(x=530,y=555)

clearimage = PhotoImage(file='clear.png')
clearbutton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=clear)
clearbutton.place(x=660, y=555)

exitimage = PhotoImage(file='exit.png')
exitbutton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=iexit)
exitbutton.place(x=790, y=555)







root.mainloop()                                                  #It will hold the window.

