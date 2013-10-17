import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
from matplotlib.backends.backend_pdf import PdfPages


f = open('gurusample.csv','r')
tinytime = []
tinycurrent = []
androidtime = []
androidcurrent = []
for line in f:
    data = line.split(',')
    t = float(data[0])
    t = t - 4802360000.0
    tinytime.append(t)
    tinycurrent.append(float(data[1]))
f.close()

ff=open('staticip.csv','r')
for line in ff:
    data = line.split(',')
    t = float(data[0])
    #t = t - 8185665000.0
    t = t - 8134965000.0
    #t = t*1000.0
    androidtime.append(t)
    androidcurrent.append(float(data[1]))

#fig,ax1 = plt.subplots()
#pylab.ylim([0,700])
#ax1.plot(time,current)
#ax1.set_xlabel('Time in Seconds.')
#ax1.set_ylabel('Current draw in mA')

'''fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax1.plot(tinytime,tinycurrent, color='blue')
ax1.set_autoscalex_on(False)
ax1.set_xlim([0,80])
ax1.set_ylabel('Current draw (mA)')
#plt.set_ylim([0,700])



ax2 = fig.add_subplot(2,1,2)
ax2.plot(androidtime,androidcurrent,color='green')
ax2.set_xlabel('Time (Seconds)')
ax2.set_ylabel('Current draw (mA)')
'''

fig, ax = plt.subplots(2, sharex=True)

ax[0].set_ylabel('Current (mA)',fontsize=10)
ax[0].plot(androidtime,androidcurrent, color='blue', linewidth=2,label='Sensor Android')
ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fontsize=10)
ax[1].set_ylabel('Current (mA)', fontsize=10)  
ax[1].plot(tinytime,tinycurrent,color='green',label='Tiny Sensor Android')
ax[1].set_xlabel('Time (Seconds)', fontsize=10)  
ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fontsize=10)
#  ax[1].legend(['AOSP','TINY_ANDROID'],'upper right', fontsize=8)


pp = PdfPages('samplecomparison.pdf')
fig.subplots_adjust(hspace=0.17, left=0.08, bottom=0.07,right=0.97, top=0.93)
from pylab import *
close()
pp.savefig(fig)
pp.close()

#:wplt.show()
