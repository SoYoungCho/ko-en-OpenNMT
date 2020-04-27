from tkinter import *
import tkinter.messagebox
from onmt.bin.translate import main

class main2:
    def __init__(self,window):
        self.window = window
        self.window.title("한영 번역기")
        self.window.resizable(False, False)
        self.transInput()

    def transInput(self):
        self.f1 = Frame(self.window, height=400)
        self.f1.grid(row=0, column=0)
        self.f2 = Frame(self.window, height=400)
        self.f2.grid(row=0, column=1)
        self.f3 = Frame(self.window, height=100)
        self.f3.grid(row=1, column=0, columnspan=2)

        self.l1 = Label(self.f1, text="[ 한글 ]", font=("맑은 고딕", 15,"bold"), width=30)
        self.l1.grid(row=0, column=0, pady=10)
        self.tb1 = Text(self.f1, width=40, wrap="word")
        self.tb1.grid(row=1, column=0)
        self.sl1 = Scrollbar(self.f1)
        self.sl1.grid(row=1, column=1,sticky=N+S+W)
        self.sl1.config(command=self.tb1.yview)
        self.tb1.config(yscrollcommand=self.sl1.set)


        self.l2 = Label(self.f2, text="[ 영어 ]", font=("맑은 고딕", 15,"bold"), width=30)
        self.l2.grid(row=0, column=0, pady=10)
        self.tb2 = Text(self.f2, width=40, wrap="word")
        self.tb2.grid(row=1, column=0)
        self.sl2 = Scrollbar(self.f2)
        self.sl2.grid(row=1, column=1, sticky=N + S+W)
        self.sl2.config(command=self.tb2.yview)
        self.tb2.config(yscrollcommand=self.sl2.set)

        self.tran=Button(self.f3, text="번역", command=self.trans)
        self.tran.pack(pady=10)

    def isHangul(self, text):
        hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
        return hanCount > 0

    def trans(self):
        if self.isHangul(self.tb1.get('1.0', 'end')):
            f = open("src.txt", 'w', encoding="utf-8")
            f.write(self.tb1.get('1.0', 'end'))
            f.close()
            main()
            f = open("pred.txt", 'r')
            line=f.read()
            f.close()
            self.tb2.delete('1.0', 'end')
            self.tb2.insert(1.0,line)
        else:
            tkinter.messagebox.showwarning("입력","한글이 아닌 문자가 입력되었습니다.\n다시 입력하세요")


window=Tk()
main2(window)
window.mainloop()