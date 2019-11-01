from tkinter import *


def export_tweet():
    'Ingevoerde text van 140 karakters in bericht.txt opslaan'
    input = textbox.get("1.0",END) # get het inhoud van Text widget
    txt = input.strip() # verwijder whitespaces , \n
    while True:
        if len(txt) >= 140:
            textbox.config(state=NORMAL)
            textbox.delete(1.0, END) # verwijder inhoud in text widget
            warning_posted.config(text='Tweet moet minder dan 140 karakters bevatten'
                                     'remove written tekst and try again')
            break
        else:
            # Voeg bericht toe in bericht.txt
            infile = open('bericht.txt', 'a')
            infile.write('{}\n'.format(txt))
            infile.close()

            textbox.destroy() # verwijder text widget
            warning_posted.config(text='Thank you.If approved, you can see your tweet at ns_consumenteezuil account')
            break




root = Tk()



intro = Label(root, text= 'Write a tweet !')
intro.pack(side=TOP, padx=10, pady=10)

textbox = Text(root, width=20, height=10)
textbox.pack(side=TOP,fill = X)

warning_posted = Label(root, width= 100)
warning_posted.pack(side=BOTTOM, fill= Y )

tweetbutton = Button(root, text='tweet' ,command=export_tweet)
tweetbutton.pack(side=BOTTOM,padx=20, pady=20)

root.mainloop()