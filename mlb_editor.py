import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    #mlb_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    #mlb_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Frame_button = Frame(top)
        self.Frame_button.place(relx=0.02, rely=0.04, relheight=0.5
                , relwidth=0.41)
        self.Frame_button.configure(relief=GROOVE)
        self.Frame_button.configure(borderwidth="2")
        self.Frame_button.configure(relief=GROOVE)
        self.Frame_button.configure(background="#d9d9d9")
        self.Frame_button.configure(width=245)

        self.fra38_but39 = Button(self.Frame_button)
        self.fra38_but39.place(relx=0.08, rely=0.07, height=30, width=200)
        self.fra38_but39.configure(activebackground="#d9d9d9")
        self.fra38_but39.configure(activeforeground="#000000")
        self.fra38_but39.configure(background="#d9d9d9")
        self.fra38_but39.configure(compound="center")
        self.fra38_but39.configure(disabledforeground="#a3a3a3")
        self.fra38_but39.configure(foreground="#000000")
        self.fra38_but39.configure(highlightbackground="#d9d9d9")
        self.fra38_but39.configure(highlightcolor="black")
        self.fra38_but39.configure(pady="0")
        self.fra38_but39.configure(text='''List all Recipe''')
        self.fra38_but39.configure(width=282)

        self.button_lt = Button(self.Frame_button)
        self.button_lt.place(relx=0.08, rely=0.27, height=30, width=200)
        self.button_lt.configure(activebackground="#d9d9d9")
        self.button_lt.configure(activeforeground="#000000")
        self.button_lt.configure(background="#d9d9d9")
        self.button_lt.configure(compound="center")
        self.button_lt.configure(disabledforeground="#a3a3a3")
        self.button_lt.configure(foreground="#000000")
        self.button_lt.configure(highlightbackground="#d9d9d9")
        self.button_lt.configure(highlightcolor="black")
        self.button_lt.configure(pady="0")
        self.button_lt.configure(text='''List by Type''')
        self.button_lt.configure(width=282)

        self.button_ar = Button(self.Frame_button)
        self.button_ar.place(relx=0.08, rely=0.49, height=30, width=200)
        self.button_ar.configure(activebackground="#d9d9d9")
        self.button_ar.configure(activeforeground="#000000")
        self.button_ar.configure(background="#d9d9d9")
        self.button_ar.configure(compound="center")
        self.button_ar.configure(disabledforeground="#a3a3a3")
        self.button_ar.configure(foreground="#000000")
        self.button_ar.configure(highlightbackground="#d9d9d9")
        self.button_ar.configure(highlightcolor="black")
        self.button_ar.configure(pady="0")
        self.button_ar.configure(text='''Add Recepi''')
        self.button_ar.configure(width=282)

        self.button_ar_1 = Button(self.Frame_button)
        self.button_ar_1.place(relx=0.08, rely=0.71, height=30, width=200)
        self.button_ar_1.configure(activebackground="#d9d9d9")
        self.button_ar_1.configure(activeforeground="#000000")
        self.button_ar_1.configure(background="#d9d9d9")
        self.button_ar_1.configure(compound="center")
        self.button_ar_1.configure(disabledforeground="#a3a3a3")
        self.button_ar_1.configure(foreground="#000000")
        self.button_ar_1.configure(highlightbackground="#d9d9d9")
        self.button_ar_1.configure(highlightcolor="black")
        self.button_ar_1.configure(pady="0")
        self.button_ar_1.configure(text='''Edit Recepi''')
        self.button_ar_1.configure(width=282)

        self.Text1 = Text(top)
        self.Text1.place(relx=0.45, rely=0.07, relheight=0.3, relwidth=0.19)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=114)
        self.Text1.configure(wrap=WORD)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.02, rely=0.62, relheight=0.17, relwidth=0.41)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=245)

        self.button_save = Button(self.Frame2)
        self.button_save.place(relx=0.08, rely=0.4, height=24, width=84)
        self.button_save.configure(activebackground="#d9d9d9")
        self.button_save.configure(activeforeground="#000000")
        self.button_save.configure(background="#d9d9d9")
        self.button_save.configure(disabledforeground="#a3a3a3")
        self.button_save.configure(foreground="#000000")
        self.button_save.configure(highlightbackground="#d9d9d9")
        self.button_save.configure(highlightcolor="black")
        self.button_save.configure(pady="0")
        self.button_save.configure(text='''save''')
        self.button_save.configure(width=84)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.53, rely=0.4, height=24, width=69)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''exit''')
        self.Button3.configure(width=69)






if __name__ == '__main__':
    vp_start_gui()