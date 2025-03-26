# practica GUI

import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from argparse import Action

# crear instancia
win = tk.Tk()
#add a table
win.title('python GUI')

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='tab 2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='tab3')

tabControl.pack(expand=1, fill='both')

mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

mighty2 = ttk.LabelFrame(tab2, text=' the snake')
mighty2.grid(column=0, row=0, padx=0, pady=4)



#redimencionar con true o false
win.resizable(True, True)

#ttk.Label(win, text= 'pon tu nombre:').grid(column=0, row=0)

a_label = ttk.Label(mighty, text='pon tu nombre' )
a_label.grid(column=0, row=0, sticky=tk.E)

def ClickMe():
    action.configure(text='hola ' + name.get() + ' ' + numberChosem.get())
    a_label.configure(foreground='blue')
    #a_label.configure(text= 'A Red Label') 

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(mighty, text= 'presioname', command=ClickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')

ttk.Label(mighty, text='escoge un numero:').grid(column=1, row=0) 
number = tk.StringVar
numberChosem = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
numberChosem['values'] = (1, 2, 4, 42, 100)
numberChosem.grid(column=1, row=1)
numberChosem.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text='disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text='unChecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarIn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text='enabled', variable=chVarIn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)
name_entered.focus()

chVarDis2 = tk.IntVar()
check4 = tk.Checkbutton(mighty2, text='disabled', variable=chVarDis, state='disabled')
check4.select()
check4.grid(column=0, row=4, sticky=tk.W)

chVarUn2 = tk.IntVar()
check5 = tk.Checkbutton(mighty2, text='unChecked', variable=chVarUn)
check5.deselect()
check5.grid(column=1, row=4, sticky=tk.W)

chVarIn2 = tk.IntVar()
check6 = tk.Checkbutton(mighty2, text='enabled', variable=chVarIn)
check6.select()
check6.grid(column=2, row=4, sticky=tk.W)
name_entered.focus()

colors =['Blue', 'Gold', 'Red','Black', 'Pink', 'Green','Blue', 'Gold', 'Red','Blue', 'Gold', 'Red']

def radCall():
    radSel=radVar.ger()
    if    radSel == 0:win.configure(background=colors[0])
    elif  radSel == 1:win.configure(background=colors[1])
    elif  radSel == 2:win.configure(background=colors[2])
    elif  radSel == 3:win.configure(background=colors[3])
    elif  radSel == 4:win.configure(background=colors[4])
    elif  radSel == 5:win.configure(background=colors[5])
    elif  radSel == 6:win.configure(background=colors[6])
    
radVar = tk.IntVar()

radVar.set(99)
for col in range(3):
    curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

radVar.set(99)
for col in range(6):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)
    
#rad1 = tk.Radiobutton(win, text=color1, variable=radVar, value=1, command=radCall)
#rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3) }

#rad2 = tk.Radiobutton(win, text=color2, variable=radVar,value=2, command=radCall)
#rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3) 

#radVar = tk.IntVar()
#rad3 = tk.Radiobutton(win, text=color3, variable=radVar, value=3, command=radCall)
#rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3) 

scrol_w = 30
scrol_h = 5
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

buttons_frame = ttk.Labelframe(mighty, text= 'labels is a frame')
buttons_frame.grid(column=1, row=7, padx=20, pady=40)

ttk.Label(buttons_frame, text='label1').grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text='label2').grid(column=1, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text='label3').grid(column=2, row=2, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

menu_bar = Menu(win)
win.config(menu=menu_bar)

def _quit():
    win.quit()
    win.destroy()
    exit()

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='nuevo')
file_menu.add_separator()
file_menu.add_command(label='salir', command=_quit)
menu_bar.add_cascade(label='file', menu=file_menu)

help_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='help',menu=help_menu)
help_menu.add_command(label='about')

cat_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='gatos',menu=cat_menu)
cat_menu.add_separator()
cat_menu.add_command(label= 'tomas')
cat_menu.add_command(label='kitty')
cat_menu.add_command(label='chuleta', command=_quit)


name_entered.focus()
 #INICIAR gui
win.mainloop() 