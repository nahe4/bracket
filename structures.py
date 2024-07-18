import numpy as np

import bracket
import functions
import tkinter as tk
from tkinter import ttk

'''class Base():
    def __init__(self):
        self.Teamsin=False
        self.s_or_u = True
        self.elimnumber = False'''


class Unseeded():
    def __init__(self, parent, teams):
        #self.teams={}

        print('unseeded')


#b=Unseeded()

class Seeded():
    def __init__(self, parent, teams):
        self.teamseeds={}
        #for n in rawteams:

        print('seeded')

class SingleElim():
    def __init__(self, parent):
        #super().__init__()
        print('hallelujah')



        #bracket variables
        self.teams = {1: 'team1', 2: 'team2', 3: 'team3', 4: 'team4', 5: 'team5', 6: 'team6', 7: 'team7', 8: 'team8'}
        lenteams = len(self.teams)
        #bracketsize = np.log(2, 8)

        #menu widgets to initialize in UI_items.Menu
        #self.teamsin=True
        self.s_or_u=True
        self.elimnumber=False


        #teams={1:'team1', 2:'team2', 3:'team3', 4:'team4', 5:'team5', 6:'team6', 7:'team7', 8:'team8'}
        #lenteams=len(teams)
    def showbracket(self, seeded):
        if seeded==True:
            s=Seeded(self, self.teams)
            print('showing seeded bracket')
        else:
            s=Unseeded(self, self.teams)
            print('showing unseeded bracket')



class DoubleElim():
    def __init__(self, parent):
        print('b2elim')

class RoundRobin():
    def __init__(self, parent):
        print('roundrobin')

class GroupStage():
    def __init__(self, parent):
        print('Groupstage')


#print('base teams',b.teams)