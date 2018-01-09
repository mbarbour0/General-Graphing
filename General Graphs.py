from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import datetime as datetime

user_selection = raw_input('Select the type of graph you would like to use.\nLine Graph\nBar Graph\nPie Chart\nHistogram\n>>>')
us = user_selection.lower()
print 'You have selected to use a %s.' % (us)
if us in ['line graph', 'bar graph', 'histogram']:
    xplot = raw_input('Select 1, 2, or 3 for the X Plot: \n>>>')

def graph():
    

plt.plot(range(5), range(5))