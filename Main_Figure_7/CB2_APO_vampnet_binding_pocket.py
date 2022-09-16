import pickle
import pyemma
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import glob
import mdtraj as md
from matplotlib import rc
import numpy as np 
import matplotlib.cm
import sys

hfont = {'fontname':'Helvetica'}
rc('text', usetex=True)
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

def rgb_to_hex(r, g, b):
    return ('#{:02X}{:02X}{:02X}').format(r, g, b)


def scatter_plot(volume,distance,label,color):
    sc = axs.scatter(distance,volume,c=color,s=60,label=label)

if __name__=='__main__':
    volume = np.zeros([6,100])
    distance = np.zeros([6,100])
    
    states = ['3','0','1','2','4','5']
    labels = ['Inactive','I1','I2','I3','I4','Active']

    fig, axs = plt.subplots(1,1,figsize=(10,7))
    for j,state in enumerate(states):
        volume[j,:] = pickle.load(open('./CB2_macrostate_'+state+'_volume_cal.pkl','rb'))
        distance[j,:] = pickle.load(open('./CB2_macrostate_'+state+'_N-terminus_distance.pkl','rb'))
        scatter_plot(volume[j,:],distance[j,:]*10,labels[j],rgb_to_hex(int(255*(0.0+0.9/5*j)),int(255*(1.0-1.0/5*j)),int(255*(0.0+0.38/5*j))))
    
    plt.xlabel('N-terminus Distance (\AA) ',fontsize=30)
    plt.ylabel('Volume ($\AA^3$)',fontsize=30)
    plt.xlim([10,40])
    plt.ylim([0,200])
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.tight_layout()
    plt.legend(fontsize=18)
    plt.savefig('CB2_pocket_volume',transparent=False,dpi =500)
    
    plt.close()

    #scatter_plot(txx)
    #box_plot(txx)


