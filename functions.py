from tkinter import filedialog
import csv
import structures as s
def readfile():
    out = {}
    with open(str(filedialog.askopenfilename(filetypes=[('csv', '.csv'), ('dmg', '.dmg')])), newline='') as csvfile:
        # print(csv.reader(csvfile, delimiter=',', quotechar='|'))
        reader = csv.reader(csvfile, delimiter=',')
        for rows in reader:
            out[rows[0]]=rows[1]
            print('test', rows)
        #print(s.Unseeded.teams)

#def start(seeds, teams, size):
    #format=structures.seeds()
