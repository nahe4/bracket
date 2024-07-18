import tkinter
from tkinter import ttk
import functions
import numpy as np
import structures


class Selection(ttk.Combobox):
    def __init__(self, parent, vals):
        self.curstruc = tkinter.StringVar()
        self.curstruc.set('n')
        ttk.Combobox.__init__(self, parent, state='readonly', textvariable=self.curstruc, values=vals)
        #curstruc=self.get()
        self.bind('<<ComboboxSelected>>', lambda event: self.value())
    def value(self):
        #self.curstruc.set(self.get())
        print('v',self.curstruc.get())
        return self.curstruc.get()

class Graphic(tkinter.Canvas):
    def __init__(self, parent, size):
        self.width=200*size
        self.height=30*(2**size)  #account for exponential height growth
        tkinter.Canvas.__init__(self, parent, width=self.width, height=self.height, background='white')
        i=0
        self.game_instances={}
        #self.games={} #Keys: integer id for each game// Vals: list of teams in that game

        for n in range(size):
            right = self.width - (n * 100)
            left=n*100
            step=30*(2**(n+1)) #vertical distance between bracket strands in stage n
            for k in range(0, self.height, step):
                self.create_line(right, k+step/2, right - 100, k+step/2, fill='black', width=3)
                self.create_line(left, k+step/2, left + 100, k+step/2, fill='black', width=3)


                if (k/step)%2==0 and (n+1)<size:
                    self.create_line(right-100, k+step/2, right-100, k + 3*step/2, fill='black', width=3)
                    self.create_line(left+100, k+step/2, left+100, k + 3*step/2, fill='black', width=3)
    def play(self, size, round, teams):

        self.game_instances[round]={}
        i=1
        for n in range(round):
            right = self.width - (n * 100)
            left = n * 100
            step = 30 * (2 ** (n + 1))
            for k in range(0, self.height, 2*step):
                if n == round - 1:
                    if round<size:
                        self.game_instances[round][i] = ButtonFrame(parent=self,
                                                x=right - 50,
                                                y=k + step/2+30*2**(round-1),
                                                teams=teams[round][i],
                                                id=(round,i),
                                                round=round, final=False)
                        self.game_instances[round][i+1] = ButtonFrame(parent=self,
                                                x=left + 50,
                                                y=k + step/2+30*2**(round-1),
                                                teams=teams[round][i+1],
                                                id=i+1,
                                                round=round, final=False)
                        i += 2
                    elif round==size: #Final round
                        print("finals")
                        self.game_instances[round][i] = ButtonFrame(parent=self,
                                                        x=right - 50,
                                                        y=k+step/2,
                                                        teams=teams[round][i],
                                                        round=round, id=i, final=True)

        def nextround():
            out=[]
            #print(self.game_instances)
            for match in self.game_instances[round].values():
                if match.winner.get():
                    out.append(match.winner.get())
                #match.cock.config(text='')

            #print(out)

            if len(out)==2**(size-round): #verify user has selected a winner for each game
                t=1
                temp=out
                teams[round+1]={}
                while temp:
                    if len(temp)>=4:
                        teams[round+1][t]=[temp.pop(0),temp.pop(1)]
                        teams[round+1][t+1] = [temp.pop(0), temp.pop(0)]
                    elif len(temp)==2:
                        teams[round+1][t] = [temp.pop(0), temp.pop(0)]
                    else:
                        teams[round + 1][t] = [temp.pop(0)]
                    t+=2
                print('tdict',teams)
                if round < size:
                    for match in self.game_instances[round].values():
                        match.cock.config(textvariable='')
                    return self.play(size, round+1, teams)
                elif round==size:
                    print('ended', self.game_instances)
                    self.delete("all")
                    self.winframe=tkinter.Frame(self, bg='blue')
                    self.create_window(self.width/2, self.height/2, window=self.winframe)
                    self.winframe.tkraise()
                    self.winning_team=tkinter.Label(self.winframe, text=self.game_instances[round][1].winner.get()+" has won the tournament!", highlightcolor='green')
                    self.winning_team.pack()
                    #self.reset=ttk.Button(text='reset', command=play(self, parent, ))
                    return self.winning_team
                    #self.winning_team.tkraise()
                    #self.winning_team
            else:
                # return self.play(size, round, teams)
                print('select all teams')



        next = tkinter.Frame(self)
        self.create_window(self.width / 2, self.height*(3/4), window=next)
        d = tkinter.Button(next, text='Next Round', command=nextround)
        d.pack()

        def reset():
            self.delete()

        resetframe = tkinter.Frame(self)
        self.create_window(self.width / 2, self.height / 4, window=reset)
        d = tkinter.Button(next, text='reset', command=nextround)
        d.pack()
    #def reset(self):




class ButtonFrame(tkinter.Frame):
    def __init__(self, parent, x, y, teams, id, round, final):
        super().__init__(parent, bg='white')
        team1 = teams[0]
        team2 = teams[1]
        self.winner=tkinter.StringVar(name=str(id))
        self.winner.set('')
        if final==False:
            parent.create_window(x, y, window=self)
        else:
            parent.create_window(x-50, y, window=self)
        self.b1 = ttk.Button(self, text=team1, command=lambda: self.winner.set(team1))
        self.b2 = ttk.Button(self, text=team2, command=lambda: self.winner.set(team2))
        self.cock = tkinter.Label(self, textvariable=self.winner)
        if final==False:
            self.b1.pack()
            self.cock.pack(pady=30*(2**(round-1))-25)
            self.b2.pack()
        else:
            self.b1.pack(side='left')
            self.b2.pack(side='left')
            self.cock.pack(side='top', pady=30)

    #def get(self):
        #if self.winner:
            #return self.winner
class Scrollbar(ttk.Scrollbar):
    def __init__(self, parent, side, command):
        tkinter.Scrollbar.__init__(self, parent, command=command)
        #self.config()
        #self.pack(side = side)





class Menu(ttk.Frame):
    def __init__(self, parent, controller, s_or_u, elimnumber):
        ttk.Frame.__init__(self, parent)

        importbutton = ttk.Button(self, text='Imp', command=functions.readfile)
        importbutton.pack()

        if s_or_u==True:
            checkbox = ttk.Checkbutton(self, text='seeded?', variable=parent.is_seeded, onvalue=True,
                        offvalue=False)
            checkbox.pack()

        if elimnumber==True:
            entry = ttk.Entry(self, width=5)
            entry.pack()
        startbutton=ttk.Button(self, text='start', command=parent.showbracket).pack()
#class Menu(ttk.Frame):

