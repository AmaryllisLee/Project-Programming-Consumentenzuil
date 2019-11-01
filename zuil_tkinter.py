from tkinter import *
from tkinter.messagebox import showinfo


def export_tweet():
    input = textbox.get("1.0",END)
    txt = input.strip()
    while True:
        if len(txt) >= 140:
            textbox.config(state=NORMAL)
            textbox.delete(1.0, END)
            warning_posted.config(text='Tweet moet minder dan 140 karakters bevatten'
                                     'remove written tekst and try again')
            break
        else:
            infile = open('bericht.txt', 'a')
            infile.writelines(txt)
            infile.close()
            textbox.destroy()
            warning_posted.config(text='Thank you.If approved, you can see your tweet at ... account')
            break




root = Tk()


#zuilframe = Frame(master=root)
#zuilframe.pack(fill="both", expand=True)


textbox = Text(root, width=20, height=10)
#textbox.pack(padx=20, pady=20)
textbox.pack(side=TOP,fill = X)

warning_posted = Label(root, width= 100)
warning_posted.pack(side=BOTTOM, fill= Y )

tweetbutton = Button(root, text='tweet' ,command=export_tweet)
tweetbutton.pack(side=BOTTOM,padx=20, pady=20)

root.mainloop()