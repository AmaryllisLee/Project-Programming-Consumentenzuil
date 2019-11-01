from tkinter import *
import datetime
from TwitterAPI import TwitterAPI

consumer_key='GtWhGAVYvrZeP7VmBtpRjIZVo'
consumer_secret = 'OWrWYT6tFZnYfY5f1rhg9vqmB0xTDqxH80wh08pDXQ2WgnLbhr'
acces_token='1190032239523971072-fSe9YWof8V9dC6NmGc7KHVzgRLqnEP'
acces_secret ='RoBAukgCsWL4koLfrjFtdqt4jrffiNAUbPWQ6UWgHjEVI'

api = TwitterAPI(consumer_key,consumer_secret,acces_token,acces_secret)

# r = api.request('statuses/update', {'status':'This is the first tweet!'})
# print(r.status_code)


def bericht_checken():
    with open('bericht.txt') as r:
        lines = r.readlines()
    r.close()
    return lines

def login():
    accepted_tweets=[]

    current_line= 0

    vandaag = datetime.datetime.today()  # geeft de datum and tijd van vandaag
    time = vandaag.strftime("%a %d %b %Y, %I:%M:%S")

    if loginfield.get() == "admin":
        wrong_pw.config(text='You are logged in.Please close Window')

        lines = bericht_checken() #  berichten uit bericht.txt

        while current_line<len(lines):
            controle= input('{} accept or reject? '.format(lines[current_line])) # bericht accepteren of weigeren

            if controle == 'accept':
                r = api.request('statuses/update', {'status': lines[current_line]}) # bericht lines(current_line) wordt op Twitter gepost
                print('posted' if r.status_code == 200 else 'PROBLEM' + r.text)

                # Tijdelijke solution voor recente tweets
                accepted_tweets.append(lines[current_line])

                current_line+=1

            elif controle == 'reject':
                reason = input('Waarom ? ') # geeft opmerking van het bericht

                vandaag = datetime.datetime.today() # geeft de datum and tijd van vandaag
                time = vandaag.strftime("%a %d %b %Y, %I:%M:%S")

                # Geweigerde bericht , opmerking en de datum en tijd worden opgeslagen in logfile.txt
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