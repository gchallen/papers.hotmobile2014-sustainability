#!/usr/bin/env python

import csv,sys,re
import matplotlib.cm as cm
from datetime import *
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import os
import numpy as np


from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times'],'size':'10'})
rc('text', usetex=True)

timeAxis1 = []
batAxis1 = []
luxAxis1 = []

line_pattern = re.compile(ur"""^(?x)
                          (?P<datetime>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+
                          (?P<power>[\d\.]+)\s+
                          (?P<light>[\d\.]+)""")
datetime_pattern = '%Y-%m-%d %H:%M:%S'

for line in open(sys.argv[1], 'r'):
  line_match = line_pattern.match(line)
  if line_match == None:
    continue
  timeAxis1.append(datetime.datetime.strptime(line_match.group('datetime'), datetime_pattern))
  batAxis1.append(float(line_match.group('power')) * 100.)
  luxAxis1.append(float(line_match.group('light')))

timeAxis2 = []
batAxis2 = []
luxAxis2 = []

line_pattern = re.compile(ur"""^(?x)
                          (?P<datetime>\w{3}\s\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\s\w{3}\s\d{4})\s+
                          (?P<power>[\d\.]+)\s+
                          (?P<light>[\d\.]+)""")
datetime_pattern = '%a %b %d %H:%M:%S %Z %Y'

for line in open(sys.argv[2], 'r'):
  line_match = line_pattern.match(line)
  if line_match == None:
    continue
  timeAxis2.append(datetime.datetime.strptime(line_match.group('datetime'), datetime_pattern))
  batAxis2.append(float(line_match.group('power')))
  luxAxis2.append(float(line_match.group('light')))

fig, ax = plt.subplots(2, sharex=True)

ax[0].grid()
ax[0].set_ylabel('Battery Level',fontsize=10)
ax[0].plot(timeAxis1,batAxis1, color='blue', linewidth=2,
           label=r'{\small \textbf{Sensor Android}}')
ax[0].plot(timeAxis2,batAxis2, color='green', linewidth=2,
           label=r'{\small \textbf{Tiny Sensor Android}}')
ax[0].set_autoscaley_on(False)
ax[0].set_ylim([0,100])
ax[0].legend(loc='upper right')
ax[1].grid()
ax[1].set_ylabel(r'{\small \textbf{Light Level}}', fontsize=10)  
ax[1].set_xlabel(r'{\small \textbf{Date}}', fontsize=10)  
ax[1].plot(timeAxis1,luxAxis1,color='blue')
ax[1].plot(timeAxis2,luxAxis2, color='green')
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
ax[1].xaxis.set_major_locator(mdates.DayLocator());
ax[1].axis(ymin=0,ymax=110)

fig.subplots_adjust(hspace=0., left=0.07, bottom=0.08,right=0.99, top=0.99)
close()
fig.savefig('comparison.pdf')
