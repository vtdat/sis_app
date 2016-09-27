import Tkinter as tk
import os
import tkMessageBox

import sys

import main
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        entryaccount = tk.Entry(self, exportselection=0)
        entrypassword = tk.Entry(self, exportselection=0, show='*')
        labelaccount = tk.Label(self, text='MSSV', anchor=tk.W)
        labelpassword = tk.Label(self, text='Password')
        labelaccount.grid(column=0, row=0)
        labelpassword.grid(column=0, row=1)
        entryaccount.grid(column=2, row=0)
        entrypassword.grid(column=2, row=1)
        textlabel = tk.StringVar()
        entryaccount.focus_set()
        textlabel.set('Your CPA will appear here!')
        labelresult = tk.Label(self, textvariable = textlabel)
        labelresult.grid(column=0, row = 4, columnspan=3)
        getbutton = tk.Button(self, text='Get CPA', command= lambda: self.OnButtonClick(entryaccount.get(), entrypassword.get(), textlabel))
        getbutton.grid(column=0, row=3, pady=5, columnspan=3)
        entrypassword.bind("<Return>", lambda x: self.OnButtonClick(entryaccount.get(), entrypassword.get(), textlabel))

    def OnButtonClick(self, username, password, textlabel):
        if username != '' and password != '':
            tkMessageBox.showinfo('', "Please wait!!")
            cpaResult = main.calCPa(username, password)
            if cpaResult == -1:
                tkMessageBox.showinfo('', "Either server is busy or you've provided invalid information.\nPlease try again!!")
            else:
                textlabel.set('Your CPA = ' + str(cpaResult))
        elif not username.isdigit():
            tkMessageBox.showinfo('', "Wrong username!")
        else:
            tkMessageBox.showinfo('', "Username or password is missing!!")


def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x-100, y-100)))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = Application()
    app.master.title('')
    app.master.resizable(0,0)
    app.master.iconbitmap(resource_path('logo.ico'))
    center(app.master)
    app.mainloop()

