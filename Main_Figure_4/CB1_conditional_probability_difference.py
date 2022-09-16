import numpy as np 
import os 
import fnmatch 
import pickle
import sys
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt 

hfont = {'fontname':'Helvetica'}
rc('text', usetex=True)
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

def bar_plot():
    fig, axs = plt.subplots(1,1,figsize=(14,7))
    arr = [[i,j] for i in range(5) for j in range(i+1,5)]
    mean = np.mean(bt_fraction_condition,axis=2)
    std = np.std(bt_fraction_condition,axis=2)
    
    difference_mean = np.zeros([10,2])
    difference_std = np.zeros([10,2])
    count = 0
    for i in range(5):
        for j in range(i+1,5):
            difference_mean[count,0] = np.abs(mean[i,j,0]-mean[i,j,1])
            difference_std[count,0]  = np.abs(std[i,j,0]+std[i,j,1])

            difference_mean[count,1] = np.abs(mean[j,i,0]-mean[j,i,1])
            difference_std[count,1]  = np.abs(std[j,i,0]+std[j,i,1])
            count += 1
    
    x = np.arange(0,20,2)
    
    width = 0.5 
    colors = 'b'
    axs.bar(x, difference_mean[:,0], yerr = difference_std[:,0]/10, width= width, color = colors, align='center', ecolor='black', capsize=10, alpha=0.3, edgecolor=colors, linewidth=4)

    plt.ylim(0,1)
    axs.set_xticklabels(['0|1', '0|2', '0|3','0|4','1|2','1|3','1|4','2|3','2|4','3|4'])
    axs.set_xticks(x)
    
    axs.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
    axs.set_yticklabels([0.0,0.2,0.4,0.6,0.8,1.0])

    plt.ylabel('$|P(F^{i}_{A}|F^{j}_{A})-P(F^{i}_{A}|F^{j}_{I})|$',**hfont,fontsize=24)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=22)
    plt.tight_layout()
    plt.savefig('CB1_conditional_probability_diff.png',Transperent=True,dpi=500)

if __name__=='__main__':    
    conditions = ['Helix2M_Nloop','Ex16_distance','TG_diff_z','In36_distance','In57_distance']
    features = ['Helix2M_Nloop','Ex16_distance','TG_diff_z','In36_distance','In57_distance']
    bt_numbers = 200

    bt_fraction_condition  = np.zeros([len(conditions),len(features),bt_numbers,2])

    for i,condition in enumerate(conditions):
        flag = list(range(5))
        flag.pop(i)
        filename = './CB1_'+condition+'.pkl'
        temp = pickle.load(open(filename,'rb'))
        count = 0
        for j in flag:
            bt_fraction_condition[i,j,:,:] = temp[count,:,:]
            count += 1

    bar_plot()
    
