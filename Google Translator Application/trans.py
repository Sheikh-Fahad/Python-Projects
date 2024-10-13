from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.title('Google Translator by Sheikh Fahad')
root.geometry("1080x400")
root.configure(bg='white')

#icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)



def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, label_change)
    

def translate_now():
    text = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text
    text2.delete(1.0,END)
    text2.insert(END, trans_text)
    

languages = googletrans.LANGUAGES
languageV = list(languages.values())

combo1 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='r')
combo1.place(x=100, y=20)
combo1.set('ENGLISH')

label1 = Label(root, text='ENGLISH', font='sego 30 bold', bg='white', width= 18, bd=5, relief= GROOVE)
label1.place(x=10, y=50)

f1 = Frame(root, bg='Black', bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font='Robot 20', bg='white', relief= GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height = 200)



combo2 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='r')
combo2.place(x=730, y=20)
combo2.set('SELECT LANGUAGE')

label2 = Label(root, text='ENGLISH', font='sego 30 bold', bg='white', width= 18, bd=5, relief= GROOVE)
label2.place(x=620, y=50)

f2 = Frame(root, bg='Black', bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font='Robot 20', bg='white', relief= GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height = 200)


translate_button = Button(root, text='Translate', font='Robot 15 bold italic', cursor='hand2',
                         bg='red', fg='white', command=translate_now)
translate_button.place(x=480, y=250)


label_change()
root.mainloop()