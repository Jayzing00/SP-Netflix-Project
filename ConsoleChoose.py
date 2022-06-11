#(2) Whole projet in on GitHub: https://github.com/Jayzing00/SP-Netflix-Project/tree/master
#(7) The whole code uses "procedural programming"

from matplotlib.pyplot import axis
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from pandas import *

#(3) Datatype list
#(4) Use of lists
col_list = ["Country_code", "Country", "LibrarySize", "No. of TV Shows", "No. of Movies", "CPM_Basic", "CPM_Standard", "CPM_Premium" ]

#(1) Use of real-world dataset
#(5) Use of pandas
wholeCSV = pd.read_csv('NetflixFees.csv', usecols=col_list)

cost_list = []
cpm_list = []
netflix_abos = []

df = wholeCSV.reset_index()

print("##############")
print("Möchtest du die besten oder schlechtesten Netflix-Deals anschauen?")
print("##############")
print("best = Die besten Deals")
print("worst = Die schlechtesten Deals")
print("##############")

#(6) Use of loop control statement and loop
while True:
    user_input = input()
    if user_input == "best":
        break
    elif user_input == "worst":
        break
    else: 
        print("Bitte gib worst oder best ein")

input = user_input
#(6) Use of loop
for index, row in df.iterrows():
    #Abo-Preis / Library-Size  = Kosten für *eine* einzelne Show/Film
    cost_per_content = (row.CPM_Basic / row.LibrarySize)*100
    cost_list.append(cost_per_content)
    tmp_list = [row.Country, row.LibrarySize, row.CPM_Basic, cost_per_content]
    netflix_abos.append(tmp_list)

#(5) Use of pandas
df_new = pd.DataFrame (netflix_abos, columns=["Country", "LibrarySize", "CPM_Basic" ,"cost_per_content"])
df_sort = df_new.sort_values('cost_per_content')

#(3) Datatype String
ylabel = ""
#(6) Use of conditional statement
if (input == "worst"):
    x = df_sort[60:].Country
    y = df_sort[60:].cost_per_content
    plt.xlabel("5 Worst Deals")
elif (input == "best"):
    x = df_sort[:5].Country
    y = df_sort[:5].cost_per_content
    plt.xlabel("5 Best Deals")

#(8) Use of vizualizations
plt.ylabel("Cost per Content in Cent")
plt.plot(x, y, 'o:')
plt.show()