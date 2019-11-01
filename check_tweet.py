from tkinter import *
import datetime


def bericht_checken():
    with open('bericht.txt') as r:
        lines = r.readlines()
    r.close()
    return lines

def login():
    current_line= 0
    if loginfield.get() == "admin":
        wrong_pw.config(text='You are logged in.Please close Window')

        lines = bericht_checken()
        while current_line<len(lines):
            controle= input('{} accept or reject? '.format(lines[current_line]))
            if controle == 'accept':
                print('posted')
                current_line+=1
            elif controle == 'reject':
                reason = input('Waarom ? ')

                vandaag = datetime.datetime.today()
                time = vandaag.strftime("%a %d %b %Y, %I:%M:%S")

                with open('logfile.txt', 'a') as f:
                    f.writelines('{}; {} ; {}'.format(lines[current_line], reason, time))
                f.close()
                current_line +=1
            else:
                continue
    else:
        wrong_pw.config(text='Verkeerde gebruikersnaam!')


root = Tk()

# Login page
loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)

loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)

loginbutton = Button(master=loginframe, text='login', command=login)
loginbutton.pack(padx=20, pady=20)


wrong_pw= Label(master=loginframe, width=100)
wrong_pw.pack()

root.mainloop()