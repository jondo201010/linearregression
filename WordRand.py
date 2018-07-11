from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from random import randint
import numpy as np
import pandas as pd
import os

wordFileLocation="/home/t/t/learn/python/1000Words/WordList.txt"

fullData=pd.read_csv(wordFileLocation, names=['words'],header=None)
#print(loc)
while(1):
    loc=randint(0, 999)
    print(fullData['words'][loc])
    input("")
    os.system('clear')
