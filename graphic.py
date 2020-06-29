from tkinter import *
from tree import *


def search():
    ad = fi.get()
    if len(ad.split('.')) != 4:
        nhr['text'] = 'Address invalide'
        ifc1['text'] = 'Address invalide'
    else:
        (nxt, inter) = (lookup(tree, ad)[3], lookup(tree, ad)[4])
        if nxt == '' and inter == '':
            nhr['text'] = 'Address introuvable'
            ifc1['text'] = 'Address introuvable'
        else:
            nhr['text'] = nxt
            ifc1['text'] = inter


t = Tk()
t.title('Algorithme lookup')
t.minsize(316, 720)
t.config(background='white')
f1 = Frame(t, bg='white')
c = Canvas(f1, height=316, width=316, bg='white')
img = PhotoImage(file="tree.png")
c.create_image(158, 158, image=img)
c.pack()
f1.pack()
f2 = Frame(t, bg='white')
l = Label(f2, text='Adresse IP: ', font=('Verdana', 18), fg='#5dbcd2', bg='white')
l.pack()
fi = Entry(f2, font=('Verdana', 18), fg='#49c2c9', bg='white', bd=1)
fi.pack()
f2.pack()
f3 = Frame(t, bg='white')
b = Button(f3, bd=1, font=('Verdana', 18), fg='#5dbcd2', bg='white', text='Chercher', command=search)
b.pack()
f3.pack()
f4 = Frame(t, bg='white')
nh = Label(f4, text='Next hop: ', font=('Verdana', 18), fg='#5dbcd2', bg='white')
nhr = Label(f4, text='', font=('Verdana', 18), fg='#49c2c9', bg='white')
nh.pack()
nhr.pack()
f4.pack()
f5 = Frame(t, bg='white')
ifc = Label(f5, text='Interface: ', font=('Verdana', 18), fg='#5dbcd2', bg='white')
ifc1 = Label(f5, text='', font=('Verdana', 18), fg='#49c2c9', bg='white')
ifc.pack()
ifc1.pack()
f5.pack()
t.mainloop()
