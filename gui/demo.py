
import tkinter as tk
from tkinter.messagebox import *
import datetime

class MyWindow(object):
    def __init__(self):
        self.window = tk.Tk()
        self.btn1Val = tk.StringVar()
        self.labelVal = tk.StringVar()
        self.btn = tk.Button(self.window, textvariable=self.btn1Val, command = self.btnCallBack)
        self.lable1 = tk.Label(self.window, width=4, text='666')

        self.enter = tk.Entry(self.window)
        self.btn2 = tk.Button(self.window, text="add", command=self.getInputAndInsertListToLB)

        self.listVal = tk.StringVar()
        self.listBox = tk.Listbox(self.window, listvariable=self.listVal)

        self.scale = tk.Scale(self.window, from_=5, to=23, label="try me",length=200,tickinterval=3, resolution=0.01,showvalue=1, orient=tk.HORIZONTAL, command = self.showScaleVal)
        self.chkVal = tk.IntVar()
        self.chkVal2 = tk.IntVar()
        self.checkBtn = tk.Checkbutton(self.window,text="C++",variable=self.chkVal,command=self.whetherCheck)
        self.checkBtn2 = tk.Checkbutton(self.window,text="Java",variable=self.chkVal2,command=self.whetherCheck)

    def whetherCheck(self):
        print(self.chkVal.get())
        print(self.chkVal2.get())

    def showScaleVal(self,val):
        self.lable1.config(text=val)

    def btnCallBack(self):
        # self.labelVal.set(datetime.datetime.now())
        self.lable1.config(text="230")
        answer = askquestion(title='asking',message='do you like me')
        print(answer)
        self.showItemInListBox()

    def listSelectCallBack(self,e):
        print(self.listBox.get(self.listBox.curselection()))

    def bindEvent(self):
        self.listBox.bind('<<ListboxSelect>>', self.listSelectCallBack)

    def getInputAndInsertListToLB(self):
        item = self.enter.get()
        self.listBox.insert('end',item)

    def setText(self):
        self.btn1Val.set("this is a btn")
        self.labelVal.set("None")
        self.listVal.set((11,22,33,44))

    def setWindowSize(self, sizeString):
        self.window.geometry(sizeString)

    def showItemInListBox(self):
        for i in range(self.listBox.size()):
            print(self.listBox.get(i))

    def paint(self):
        self.setWindowSize("400x400")
        self.bindEvent()
        self.enter.pack()
        self.btn2.pack()
        self.btn.pack()
        self.lable1.pack()
        self.listBox.pack()


        self.scale.pack(side='left')
        self.checkBtn.pack()
        self.checkBtn2.pack()

    def start(self):
        self.setText()
        self.paint()
        self.window.mainloop()


window = MyWindow()
window.start()





