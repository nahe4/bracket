import tkinter
from tkinter import ttk
import functions
import structures
import UI_items


class app(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.window = ttk.Frame(self, width=600, height=600)
        self.window.pack(side="top", fill="both", expand=True)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        print("11", self)

        self.frames = {} #store names of page frames

        for frm in (MainPage, Page2):
            pagename = frm.__name__
            page = frm(parent=self.window, controller=self)
            self.frames[pagename] = page #add frames and their respective page names to a dictionary
            print("frm", page)
            page.grid(row=0, column=0, sticky="nsew")


        self.showframe("MainPage")

    def showframe(self, pagename):
        frame = self.frames[pagename]
        frame.tkraise()
        #make a frame visible by raising to the front of the stacking order


class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.m = ttk.Frame(self, height=600, width=600)
        self.m.grid()
        self.m.controller = controller

        mtest=MenuFrame(self.m, controller)
        mtest.pack()

        label1 = ttk.Label(self.m, text='label', borderwidth=10)
        label1.pack(side="top", fill="x")
        label2 = ttk.Label(self.m, text='entry', borderwidth=10)
        label2.pack(side="top", fill="x", pady=10)  # grid(column=1, row=0)

        start = ttk.Button(self.m, text='next', command=lambda: controller.showframe('Page2'))
        start.pack()


class MenuFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.menu = ttk.Frame(parent)
        print("menuframe", self.menu)
        self.controller = controller
        self.i=tkinter.StringVar()
        self.i.set('SingleElim')

        self.is_seeded=True


        self.lvl2select = UI_items.Selection(self, ['SingleElim', 'DoubleElim'])
        self.lvl2select.grid(row=2, column=0)
        self.lvl2select='SingleElim'

        self.menuframes = {'SingleElim': structures.SingleElim, 'DoubleElim': structures.DoubleElim}
        self.current_structure = self.menuframes[self.lvl2select](self)

        menu = UI_items.Menu(self, self.current_structure, self.current_structure.s_or_u,
                             self.current_structure.elimnumber).grid(row=2, column=3)

        for frm in (UnseededSelect, SeededSelect):
            pagename = frm.__name__
            page = frm(parent=self, controller=parent.controller)
            self.menuframes[pagename] = page
            page.grid(row=0, column=0, sticky="nsew")
            # add frames and their respective page names to a dictionary
        
        self.showmenu("UnseededSelect")

    def showmenu(self, pagename):
        print(self.menuframes.items())
        frame = self.menuframes[pagename]
        frame.tkraise()
        # make a frame visible by raising to the front of the stacking order

    def showbracket(self):
        self.current_structure.showbracket(self.is_seeded)



class SeededSelect(ttk.Frame):
    def __init__(self, parent, controller):
        print('seededselect')
        ttk.Frame.__init__(self, parent)
        self.controller=controller
        textentry = tkinter.StringVar()

        def getteams():
            self.teams=functions.readfile()
        ttk.Entry(self, textvariable=textentry, width=5).pack()
        teamimport = ttk.Button(self, text='I', command=getteams).pack()
        quitapp = ttk.Button(self, text='2Quit', command=controller.destroy).pack()
        nextpage = ttk.Button(self, text='next',
                              command=lambda: controller.showframe('Page2')).pack()



class UnseededSelect(ttk.Frame):
    def __init__(self, parent, controller):
        print('unseededselect')
        self.lenteams=1
        ttk.Frame.__init__(self, parent)
        textentry = tkinter.StringVar()
        ttk.Entry(self, textvariable=textentry, width=5).pack()
        quitapp = ttk.Button(self, text='1Quit', command=controller.destroy).pack()
        nextpage = ttk.Button(self, text='next',
                              command=lambda: controller.showframe('Page2')).pack()


class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.f = ttk.Frame(self, height=600, width=600)
        self.f.pack()
        self.menu = ttk.Frame(self.f)
        self.menu.pack()
        self.back=ttk.Button(self.menu, text='back', command=lambda: controller.showframe('MainPage')).pack()
        self.graph=tkinter.Frame(self.f, background='red')
        self.graph.pack()

        def start():
            l = {1: {1: ['seed1', 'seed8'], 2: ['seed2', 'seed7'], 3: ['seed3', 'seed6'], 4: ['seed4', 'seed5']}}

            self.c = UI_items.Graphic(self.graph, 3)  # create a graphical bracket structure with space for 2^n teams
            self.c['scrollregion'] = self.c.bbox("all")
            self.c.grid(column=0, row=0)
            self.vscroll = UI_items.Scrollbar(self.graph, tkinter.RIGHT, self.c.yview)
            self.vscroll.grid(column=1, row=0)
            self.vscroll.lift()
            self.hscroll = UI_items.Scrollbar(self.graph, tkinter.BOTTOM, self.c.xview)
            self.c['xscrollcommand'] = self.hscroll.set
            self.c['yscrollcommand'] = self.vscroll.set


            return self.c.play(size=3, round=1, teams=l)
        self.start = ttk.Button(self, text='start', command=start)
        self.start.pack()


if __name__ == "__main__":
    mainapp = app()
    mainapp.geometry("600x600")
    mainapp.mainloop()

