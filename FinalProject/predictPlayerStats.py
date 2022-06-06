# BAL2015GL = pd.read_csv("2015BAL.EVA")

import pandas as pd
import numpy as np

file1 = open('2015SFN.EVN', 'r')
Lines = file1.readlines()
len(Lines)
cnt=0;

LineSubset = open("playerTest4.text",'w')
print('event,inning,home/away,retroSheetID,balls,strikes,play',file = LineSubset)

for i in range(len(Lines)):
    if "poseb001" in Lines[i]:
        linesplit = Lines[i].split(',')
        if linesplit[0] == 'play':
                linesplit2 = linesplit[0:4]
                linesplit2.append(linesplit[4][0])
                linesplit2.append(linesplit[4][1])
                linesplit2.append(linesplit[5])
                linesplit2.append(linesplit[6])
                cnt = cnt+1;
                print(linesplit2,file = LineSubset)

# data = pd.read_csv("playerTest2.txt")
# data
        
# column_names = ["play", "inning", "home/away","retroSheetID","balls","strikes","play"]
# playerEventMatrix = pd.DataFrame(columns = column_names)

# data = pd.read_csv("playerTest2.csv")
# data

data = pd.read_csv("playerTest4.csv")
data

posDict = {1: 'P', 2: 'C', 3: 'FB',4: 'SB', 5: 'TB', 6: 'SS',7: 'LF', 8: 'CF', 9: 'RF'}
pitchDict = {'C':'CalledStrke','S':'SwingStrike','B':'Ball','F':'Foul','X':'InPlay', ...
             'T':'foul tip','H': 'HBP','L':'FoulBunt','M': 'missedBunt','P':'pitchOut', ...
             'N':'balk','1':'pickoff1','2':'pickoff2','3':'pickoff3'}
playDict = {'S':'single','D':'double','T':'triple','H':'homeRun'}
