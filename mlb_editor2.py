#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 02, 2018 05:48:51 PM

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

#import mlb_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
  #  mlb_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
  #  mlb_support.init(w, top, *args, **kwargs)
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
        self.fra38_but39.place(relx=0.08, rely=0.42, height=30, width=200)
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

        self.Lb_numb = Label(self.Frame_button)
        self.Lb_numb.place(relx=0.08, rely=0.09, height=21, width=99)
        self.Lb_numb.configure(background="#d9d9d9")
        self.Lb_numb.configure(disabledforeground="#a3a3a3")
        self.Lb_numb.configure(foreground="#000000")
        self.Lb_numb.configure(text='''Number of recepi''')

        self.Text2 = Text(self.Frame_button)
        self.Text2.place(relx=0.16, rely=0.18, relheight=0.11, relwidth=0.22)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=54)
        self.Text2.configure(wrap=WORD)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.63, rely=0.87, relheight=0.1, relwidth=0.33)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=195)

        self.button_save = Button(self.Frame2)
        self.button_save.place(relx=0.05, rely=0.22, height=24, width=84)
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
        self.Button3.place(relx=0.56, rely=0.22, height=24, width=69)
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

        self.Fr_add = Frame(top)
        self.Fr_add.place(relx=0.02, rely=0.56, relheight=0.3, relwidth=0.96)
        self.Fr_add.configure(relief=GROOVE)
        self.Fr_add.configure(borderwidth="2")
        self.Fr_add.configure(relief=GROOVE)
        self.Fr_add.configure(background="#d9d9d9")
        self.Fr_add.configure(width=575)

        self.lb_am = Label(self.Fr_add)
        self.lb_am.place(relx=0.02, rely=0.07, height=21, width=62)
        self.lb_am.configure(background="#d9d9d9")
        self.lb_am.configure(disabledforeground="#a3a3a3")
        self.lb_am.configure(foreground="#000000")
        self.lb_am.configure(text='''Add Menu''')

        self.Lb_title = Label(self.Fr_add)
        self.Lb_title.place(relx=0.02, rely=0.22, height=21, width=34)
        self.Lb_title.configure(background="#d9d9d9")
        self.Lb_title.configure(disabledforeground="#a3a3a3")
        self.Lb_title.configure(foreground="#000000")
        self.Lb_title.configure(text='''Title:''')
        self.Lb_title.configure(width=34)

        self.ent_title = Entry(self.Fr_add)
        self.ent_title.place(relx=0.02, rely=0.37,height=20, relwidth=0.32)
        self.ent_title.configure(background="white")
        self.ent_title.configure(disabledforeground="#a3a3a3")
        self.ent_title.configure(font="TkFixedFont")
        self.ent_title.configure(foreground="#000000")
        self.ent_title.configure(insertbackground="black")
        self.ent_title.configure(width=184)

        self.lb_ingredient = Label(self.Fr_add)
        self.lb_ingredient.place(relx=0.02, rely=0.52, height=21, width=63)
        self.lb_ingredient.configure(background="#d9d9d9")
        self.lb_ingredient.configure(disabledforeground="#a3a3a3")
        self.lb_ingredient.configure(foreground="#000000")
        self.lb_ingredient.configure(text='''Ingredient:''')

        self.Entry2 = Entry(self.Fr_add)
        self.Entry2.place(relx=0.02, rely=0.67,height=40, relwidth=0.32)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=184)

        self.Lb_instruction = Label(self.Fr_add)
        self.Lb_instruction.place(relx=0.38, rely=0.22, height=21, width=63)
        self.Lb_instruction.configure(background="#d9d9d9")
        self.Lb_instruction.configure(disabledforeground="#a3a3a3")
        self.Lb_instruction.configure(foreground="#000000")
        self.Lb_instruction.configure(text='''Instruction:''')
        self.Lb_instruction.configure(width=63)

        self.Entry3 = Entry(self.Fr_add)
        self.Entry3.place(relx=0.38, rely=0.37,height=80, relwidth=0.39)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=224)

        self.rb_addbk = Radiobutton(self.Fr_add)
        self.rb_addbk.place(relx=0.82, rely=0.15, relheight=0.19, relwidth=0.14)
        self.rb_addbk.configure(activebackground="#d9d9d9")
        self.rb_addbk.configure(activeforeground="#000000")
        self.rb_addbk.configure(background="#d9d9d9")
        self.rb_addbk.configure(disabledforeground="#a3a3a3")
        self.rb_addbk.configure(foreground="#000000")
        self.rb_addbk.configure(highlightbackground="#d9d9d9")
        self.rb_addbk.configure(highlightcolor="black")
        self.rb_addbk.configure(justify=LEFT)
        self.rb_addbk.configure(text='''Breackfast''')

        self.rb_addllunch = Radiobutton(self.Fr_add)
        self.rb_addllunch.place(relx=0.8, rely=0.44, relheight=0.19
                , relwidth=0.14)
        self.rb_addllunch.configure(activebackground="#d9d9d9")
        self.rb_addllunch.configure(activeforeground="#000000")
        self.rb_addllunch.configure(background="#d9d9d9")
        self.rb_addllunch.configure(disabledforeground="#a3a3a3")
        self.rb_addllunch.configure(foreground="#000000")
        self.rb_addllunch.configure(highlightbackground="#d9d9d9")
        self.rb_addllunch.configure(highlightcolor="black")
        self.rb_addllunch.configure(justify=LEFT)
        self.rb_addllunch.configure(text='''lunch''')

        self.rb_adddinner = Radiobutton(self.Fr_add)
        self.rb_adddinner.place(relx=0.8, rely=0.3, relheight=0.19
                , relwidth=0.14)
        self.rb_adddinner.configure(activebackground="#d9d9d9")
        self.rb_adddinner.configure(activeforeground="#000000")
        self.rb_adddinner.configure(background="#d9d9d9")
        self.rb_adddinner.configure(disabledforeground="#a3a3a3")
        self.rb_adddinner.configure(foreground="#000000")
        self.rb_adddinner.configure(highlightbackground="#d9d9d9")
        self.rb_adddinner.configure(highlightcolor="black")
        self.rb_adddinner.configure(justify=LEFT)
        self.rb_adddinner.configure(text='''Dinner''')

        self.button_add = Button(self.Fr_add)
        self.button_add.place(relx=0.8, rely=0.67, height=34, width=107)
        self.button_add.configure(activebackground="#d9d9d9")
        self.button_add.configure(activeforeground="#000000")
        self.button_add.configure(background="#d9d9d9")
        self.button_add.configure(disabledforeground="#a3a3a3")
        self.button_add.configure(foreground="#000000")
        self.button_add.configure(highlightbackground="#d9d9d9")
        self.button_add.configure(highlightcolor="black")
        self.button_add.configure(pady="0")
        self.button_add.configure(text='''Add Recepi''')
        self.button_add.configure(width=107)

        self.Frame4 = Frame(top)
        self.Frame4.place(relx=0.43, rely=0.04, relheight=0.5, relwidth=0.54)
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(width=325)

        self.Lb_recipe = Listbox(self.Frame4)
        self.Lb_recipe.place(relx=0.03, rely=0.36, relheight=0.59, relwidth=0.32)

        self.Lb_recipe.configure(background="white")
        self.Lb_recipe.configure(disabledforeground="#a3a3a3")
        self.Lb_recipe.configure(font="TkFixedFont")
        self.Lb_recipe.configure(foreground="#000000")
        self.Lb_recipe.configure(width=104)

        self.text_desc = Text(self.Frame4)
        self.text_desc.place(relx=0.43, rely=0.04, relheight=0.91, relwidth=0.54)

        self.text_desc.configure(background="white")
        self.text_desc.configure(font="TkTextFont")
        self.text_desc.configure(foreground="black")
        self.text_desc.configure(highlightbackground="#d9d9d9")
        self.text_desc.configure(highlightcolor="black")
        self.text_desc.configure(insertbackground="black")
        self.text_desc.configure(selectbackground="#c4c4c4")
        self.text_desc.configure(selectforeground="black")
        self.text_desc.configure(width=174)
        self.text_desc.configure(wrap=WORD)

        self.rb_breakfast = Radiobutton(self.Frame4)
        self.rb_breakfast.place(relx=0.06, rely=0.04, relheight=0.11
                , relwidth=0.25)
        self.rb_breakfast.configure(activebackground="#d9d9d9")
        self.rb_breakfast.configure(activeforeground="#000000")
        self.rb_breakfast.configure(background="#d9d9d9")
        self.rb_breakfast.configure(disabledforeground="#a3a3a3")
        self.rb_breakfast.configure(foreground="#000000")
        self.rb_breakfast.configure(highlightbackground="#d9d9d9")
        self.rb_breakfast.configure(highlightcolor="black")
        self.rb_breakfast.configure(justify=LEFT)
        self.rb_breakfast.configure(text='''breackfast''')

        self.rb_lunch = Radiobutton(self.Frame4)
        self.rb_lunch.place(relx=0.06, rely=0.13, relheight=0.11, relwidth=0.18)
        self.rb_lunch.configure(activebackground="#d9d9d9")
        self.rb_lunch.configure(activeforeground="#000000")
        self.rb_lunch.configure(background="#d9d9d9")
        self.rb_lunch.configure(disabledforeground="#a3a3a3")
        self.rb_lunch.configure(foreground="#000000")
        self.rb_lunch.configure(highlightbackground="#d9d9d9")
        self.rb_lunch.configure(highlightcolor="black")
        self.rb_lunch.configure(justify=LEFT)
        self.rb_lunch.configure(text='''lunch''')

        self.rb_dinner = Radiobutton(self.Frame4)
        self.rb_dinner.place(relx=0.06, rely=0.22, relheight=0.11, relwidth=0.19)

        self.rb_dinner.configure(activebackground="#d9d9d9")
        self.rb_dinner.configure(activeforeground="#000000")
        self.rb_dinner.configure(background="#d9d9d9")
        self.rb_dinner.configure(disabledforeground="#a3a3a3")
        self.rb_dinner.configure(foreground="#000000")
        self.rb_dinner.configure(highlightbackground="#d9d9d9")
        self.rb_dinner.configure(highlightcolor="black")
        self.rb_dinner.configure(justify=LEFT)
        self.rb_dinner.configure(text='''Dinner''')






if __name__ == '__main__':
    vp_start_gui()



