import csv
import matplotlib.cm as cm
from datetime import *
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import os
import numpy as np



def plotBattery():
  pp = PdfPages('comparison.pdf')
  timeAxis1 = []
  batAxis1 = []
  luxAxis1 = []

  with open('sample1.tsv','r') as tsv:
    data = [line.strip().split('\t') for line in tsv]

  for item in data:
    weird_date = item[0]
    brk = weird_date.split()
    curdate = brk[5]+'-' + brk[1]+'-'+brk[2]+' '+brk[3]
    t = datetime.datetime.strptime(curdate, '%Y-%b-%d %H:%M:%S')
    timeAxis1.append(t)
    batAxis1.append(item[1])
    luxAxis1.append(item[2])

  timeAxis2 = []
  batAxis2 = []
  luxAxis2 = []

  with open('sample2.csv','r') as tsv:
    data = [line.strip().split('\t') for line in tsv]

  for item in data:
    if len(item) == 3:
    	curdate = item[0]
    	t = datetime.datetime.strptime(curdate, '%Y-%m-%d %H:%M:%S')
    	timeAxis2.append(t)
    	batAxis2.append(float(item[1])*100)
    	luxAxis2.append(item[2])

#Graph
  fig, ax = plt.subplots(2, sharex=True)
  #fig.set_size_inches( (6,6) )

  ax[0].grid()
  ax[0].set_ylabel('Battery Level',fontsize=10)
  ax[0].plot(timeAxis1,batAxis1, color='blue', linewidth=2,label='Sensor Android')
  ax[0].plot(timeAxis2,batAxis2, color='green', linewidth=2, label='Tiny Sensor Android')
  ax[0].set_autoscaley_on(False)
  ax[0].set_ylim([0,100])
  ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fontsize=10)
  ax[1].grid()
  ax[1].set_ylabel('Light Level', fontsize=10)  
  ax[1].plot(timeAxis1,luxAxis1,color='blue')
  ax[1].plot(timeAxis2,luxAxis2, color='green')
#  ax[1].legend(['AOSP','TINY_ANDROID'],'upper right', fontsize=8)
  ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
  ax[1].xaxis.set_major_locator(mdates.DayLocator());

  fig.subplots_adjust(hspace=0.07, left=0.08, bottom=0.05,right=0.99, top=0.93)
  close()
  pp.savefig(fig)
  pp.close()
