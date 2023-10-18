import pandas as pd
import matplotlib.pyplot as plt
import sys
from utils import *

print()
print()
print('*** WELCOME TO FOOTWEAR STORE MANAGEMENT SYSTEM ***')
while(True):
    print()
    print("original CSV: ->")
    df = fetchCSV()
    showCSV(df)
    showMainMenu(df)
    print()
    df = fetchCSV()
    print("Modified CSV: ->") 
    showCSV(df)
    print()
    if(input("Do U want to Continue y/n: ") == 'n') : 
        print("Thanks for Using, Have a Nice Day")
        break