from tkinter import *
from tkinter.ttk import *
from ExFramework.ExInputPort import *
from ExFramework.ExPropertyTab import *

class ExCommonTab(ExPropertyTab):
    def __init__(self, parent, name, element):
        ExPropertyTab.__init__(self, parent, name, element)
        self.pack(side=TOP)
        Label(self, text="Tag").grid(row=0, column=0, sticky=E)
        tag = Entry(self)
        tag.insert(0, self.element().tag())
        tag.configure(state='readonly')
        tag.grid(row=0, column=1)
        Label(self, text="Name").grid(row=1, column=0, sticky=E)
        ent = Entry(self)
        ent.insert(0, self.element().name())
        ent.grid(row=1, column=1)
        Label(self, text='功能概要').grid(row=2, column=0)
        text = Text(self, height=5, width=30)
        text.insert(INSERT, self.element().comment())
        text.configure(state=DISABLED)
        text.grid(row=3, columnspan=2, sticky=W)
