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
    
    difference = np.zeros([10,200,2])
    count = 0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(200):
                difference[count,k,0] = np.abs(bt_fraction_condition[i,j,k,0]-bt_fraction_condition[i,j,k,1])
                difference[count,k,1] = np.abs(bt_fraction_condition[j,i,k,0]-bt_fraction_condition[j,i,k,1])
            count += 1

    difference_mean = np.mean(difference,axis=1)
    difference_std = np.std(difference,axis=1)

    x = np.arange(0,20,2)
    width = 0.5
    colors = 'b'
    axs.bar(x, difference_mean[:,0], yerr = difference_std[:,0], width= width, color = colors, align='center', ecolor='black', capsize=10, alpha=0.4, edgecolor=None, linewidth=4)

    for i in range(len(x)):
        axs.scatter(x[i] + np.random.random(difference[i,:,0].size) * width *0.5 - width*0.5 / 2, difference[i,:,0], color='black',alpha=0.25,s=2)

    plt.ylim(0,1)
    axs.set_xticklabels(['0|1', '0|2', '0|3','0|4','1|2','1|3','1|4','2|3','2|4','3|4'])
    axs.set_xticks(x)

    axs.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
    axs.set_yticklabels([0.0,0.2,0.4,0.6,0.8,1.0])

    plt.ylabel('$|P(F^{i}_{A}|F^{j}_{A})-P(F^{i}_{A}|F^{j}_{I})|$',**hfont,fontsize=24)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=22)
    plt.tight_layout()
    plt.savefig('CB2_conditional_probability_diff.png',dpi=500)

if __name__=='__main__':
    
    conditions = ['Ex16_distance','In6_chi2','In52_distance','In36_distance','In57_distance']
    features = ['Ex16_distance','In6_chi2','In52_distance','In36_distance','In57_distance']
    bt_numbers = 200

    bt_fraction_condition  = np.zeros([len(conditions),len(features),bt_numbers,2])

    for i,condition in enumerate(conditions):
        flag = list(range(5))
        flag.pop(i)
        filename = './CB2_'+condition+'.pkl'
        temp = pickle.load(open(filename,'rb'))
        count = 0
        for j in flag:
            bt_fraction_condition[i,j,:,:] = temp[count,:,:]
            count += 1

    #print(bt_fraction_condition)
    bar_plot()
    
