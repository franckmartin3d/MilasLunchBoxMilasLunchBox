import tkinter as tk

window = tk.Tk()
window.title("Milan's Lunch Box")
window.geometry("400x400")



#-----LABEL------

label1 = tk.Label(text="Milan's Lunch Box Recepi", font=("Calibri", 20))
label1.grid(column=1, row=0)


#--------------BUTTON___________

button_up = tk.Button(text=" List all Recipe",font=("Calibri", 12))
button_up.grid(column=1, row=2)

button_up = tk.Button(text=" List by Type",font=("Calibri", 12))
button_up.grid(column=1, row=3, sticky=w)

button_up = tk.Button(text=" Add new Recipee",font=("Calibri", 12))
button_up.grid(column=1, row=4)

button_up = tk.Button(text=" Edit a Recipe",font=("Calibri", 12))
button_up.grid(column=1, row=5)

button_up = tk.Button(text=" debug display saved data",font=("Calibri", 12))
button_up.grid(column=1, row=6)

button_up = tk.Button(text=" Exit",font=("Calibri", 12))
button_up.grid(column=1, row=7)


window.mainloop()