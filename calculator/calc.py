from tkinter import*

def calc(source, side):
    storeObj =Frame (source, borderwidth = 1 ,bd = 4,bg='powder_blue')
    storeObj.pack(side=side, expand=YES , fill= BOTH)
    return storeObj

def button  (source,side,text, command =None):
    storeObj = Button(source, text=text, command= command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self,):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

    display = StringVar()
    Entry(self, relief=RIDGE,textvariable=display, justify='right',bd='powder_blue' ).pack(side=TOP, expand=YES,fill=BOTH)
