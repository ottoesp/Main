from tkinter import *
from PIL import Image, ImageTk
from Random import Random_Phrase


root = Tk()
root.geometry("1000x300")

var = IntVar()
# hang man images
death1 = Image.open("death1.png")
death1 = ImageTk.PhotoImage(death1)

death2 = Image.open("death2.png")
death2 = ImageTk.PhotoImage(death2)

death3 = Image.open("death3.png")
death3 = ImageTk.PhotoImage(death3)

death4 = Image.open("death4.png")
death4 = ImageTk.PhotoImage(death4)

death5 = Image.open("death5.png")
death5 = ImageTk.PhotoImage(death5)

death6 = Image.open("death6.png")
death6 = ImageTk.PhotoImage(death6)

death7 = Image.open("death7.png")
death7 = ImageTk.PhotoImage(death7)

win = Image.open("win.png")
win = ImageTk.PhotoImage(win)

blank = Image.open("Blank.png")
blank = ImageTk.PhotoImage(blank)

man = [death1, death2, death3, death4, death5, death6, death7, win, blank]

'''Letter Buttons'''
aBtn = Button(root, text="A", command=lambda: [GuessButton('A'), aBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
bBtn = Button(root, text="B", command=lambda: [GuessButton('B'), bBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
cBtn = Button(root, text="C", command=lambda: [GuessButton('C'), cBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
dBtn = Button(root, text="D", command=lambda: [GuessButton('D'), dBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
eBtn = Button(root, text="E", command=lambda: [GuessButton('E'), eBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
fBtn = Button(root, text="F", command=lambda: [GuessButton('F'), fBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
gBtn = Button(root, text="G", command=lambda: [GuessButton('G'), gBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
hBtn = Button(root, text="H", command=lambda: [GuessButton('H'), hBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
iBtn = Button(root, text="I", command=lambda: [GuessButton('I'), iBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
jBtn = Button(root, text="J", command=lambda: [GuessButton('J'), jBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
kBtn = Button(root, text="K", command=lambda: [GuessButton('K'), kBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
lBtn = Button(root, text="L", command=lambda: [GuessButton('L'), lBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
mBtn = Button(root, text="M", command=lambda: [GuessButton('M'), mBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
nBtn = Button(root, text="N", command=lambda: [GuessButton('N'), nBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
oBtn = Button(root, text="O", command=lambda: [GuessButton('O'), oBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
pBtn = Button(root, text="P", command=lambda: [GuessButton('P'), pBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
qBtn = Button(root, text="Q", command=lambda: [GuessButton('Q'), qBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
rBtn = Button(root, text="R", command=lambda: [GuessButton('R'), rBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
sBtn = Button(root, text="S", command=lambda: [GuessButton('S'), sBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
tBtn = Button(root, text="T", command=lambda: [GuessButton('T'), tBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
uBtn = Button(root, text="U", command=lambda: [GuessButton('U'), uBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
vBtn = Button(root, text="V", command=lambda: [GuessButton('V'), vBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
wBtn = Button(root, text="W", command=lambda: [GuessButton('W'), wBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
xBtn = Button(root, text="X", command=lambda: [GuessButton('X'), xBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
yBtn = Button(root, text="Y", command=lambda: [GuessButton('Y'), yBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))
zBtn = Button(root, text="Z", command=lambda: [GuessButton('Z'), zBtn.place_forget(), var.set(1)], width=3, height=2,
              font=("Courier", 16))

button = Button(root, text="Click Me", command=lambda: var.set(1))


def ShowLetters():
    """Shows letters"""
    qBtn.place(y=150, x=50+300)
    wBtn.place(y=150, x=80+300)
    eBtn.place(y=150, x=110+300)
    rBtn.place(y=150, x=140+300)
    tBtn.place(y=150, x=170+300)
    yBtn.place(y=150, x=200+300)
    uBtn.place(y=150, x=230+300)
    iBtn.place(y=150, x=260+300)
    oBtn.place(y=150, x=290+300)
    pBtn.place(y=150, x=320+300)
    aBtn.place(y=190, x=50+300+20)
    sBtn.place(y=190, x=80+300+20)
    dBtn.place(y=190, x=110+300+20)
    fBtn.place(y=190, x=140+300+20)
    gBtn.place(y=190, x=170+300+20)
    hBtn.place(y=190, x=200+300+20)
    jBtn.place(y=190, x=230+300+20)
    kBtn.place(y=190, x=260+300+20)
    lBtn.place(y=190, x=290+300+20)
    zBtn.place(y=230, x=50+300+40)
    xBtn.place(y=230, x=80+300+40)
    cBtn.place(y=230, x=110+300+40)
    vBtn.place(y=230, x=140+300+40)
    bBtn.place(y=230, x=170+300+40)
    nBtn.place(y=230, x=200+300+40)
    mBtn.place(y=230, x=230+300+40)


answer = []
deathCounter = 0

hangingMan = Label(root, image=man[deathCounter], height=64, width=64)
answerLabel = Label(root, text=''.join(answer), font=("Courier", 16))

errorLabel = Label(root, text="please use letters and spaces only")

def GuessButton(letter):
    """Assigns value of button to guess"""
    global guess
    guess = letter


'''Entry'''
v = StringVar()

entryButton = Button(root, text="Enter Message:",
                         command=lambda: [start()])
msgEntry = Entry(root, textvariable=v, width=50, show='*')
def entry():
    entryButton.grid(row=1, column=0, columnspan=13)
    msgEntry.grid(row=0, column=0, columnspan=12)


entry()


def AssignMsg():
    msg = v.get()
    if len(msg) == 0:
        msg = Random_Phrase()
    return msg


def start():
    if all(i.isalpha() or i.isspace() for i in AssignMsg()):
        AssignMsg()
        ShowLetters()
        entryButton.grid_forget()
        msgEntry.grid_forget()
        Hangman()
        errorLabel.grid_forget()




def Reset():
    aBtn.place_forget()
    bBtn.place_forget()
    cBtn.place_forget()
    dBtn.place_forget()
    eBtn.place_forget()
    fBtn.place_forget()
    gBtn.place_forget()
    hBtn.place_forget()
    iBtn.place_forget()
    jBtn.place_forget()
    kBtn.place_forget()
    lBtn.place_forget()
    mBtn.place_forget()
    nBtn.place_forget()
    oBtn.place_forget()
    pBtn.place_forget()
    qBtn.place_forget()
    rBtn.place_forget()
    sBtn.place_forget()
    tBtn.place_forget()
    uBtn.place_forget()
    vBtn.place_forget()
    wBtn.place_forget()
    xBtn.place_forget()
    yBtn.place_forget()
    zBtn.place_forget()
    answerLabel.place_forget()
    hangingMan.config(image=man[8])
    resetBtn.place_forget()
    entry()


resetBtn = Button(root, text="Play again?", font=('courier', 16),
                  command=lambda: [Reset()])



def Hangman():
    usedLetters = []
    msg = list(AssignMsg())
    answer = []
    for x in msg:
        answer.append(x.lower())
    length = len(msg)
    if all(i.isalpha() or i.isspace() for i in answer):
        for i in range(length):
            if msg[i] != ' ':
                msg[i] = '_'
        stopper = 0
        msgLabel = Label(root, text=''.join(msg), font=("Courier", 16))
        msgLabel.place(x=800 / 2, y=100)
        deathCounter = 0

        hangingMan.place(y=30, x=800 / 2)
        while stopper != 1:
            if '_' in msg:
                hangingMan.config(image=man[deathCounter])
                msgLabel.configure(text=''.join(msg))
                button.wait_variable(var)
                var.set(1)
                global guess
                guess = guess.lower()
                usedLetters.append(guess)
                if guess in answer:
                    for i in range(len(answer)):
                        if guess == answer[i]:
                            msg[i] = guess
                else:
                    deathCounter = deathCounter + 1
                    if deathCounter == 6:
                        msgLabel.place_forget()
                        answerLabel.config(text=''.join(answer))
                        answerLabel.place(x=800 / 2, y=100)
                        hangingMan.configure(image=man[6])

                        resetBtn.place(x=800 / 2, y=0)
                        stopper = 1
            else:
                hangingMan.configure(image=man[7])

                msgLabel.place_forget()
                answerLabel.config(text=''.join(answer))
                answerLabel.place(x=800 / 2, y=100)
                resetBtn.place(x=800 / 2, y=0)
                stopper = 1
    else:
        Reset()


root.mainloop()
