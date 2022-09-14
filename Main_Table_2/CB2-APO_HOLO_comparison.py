import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import glob
import pickle
from matplotlib import rc
import sys

def kl_divergence(p, q):
    kl_div = 0
    for i in range(len(p)):
        if not(p[i] == 0 or q[i] == 0):
            kl_div += p[i] * np.log2(p[i]/q[i])
    return kl_div

def kl_calculation(x_data,y_data):
    minimum = max([np.min(x_data),np.min(y_data)])
    maximum = min([np.max(x_data),np.max(y_data)])
    bins = np.arange(minimum,maximum,(maximum-minimum)/100)
    xhist,xedges = np.histogram(x_data,bins=bins,density=True)
    yhist,yedges = np.histogram(y_data,bins=bins,density=True)
    x_prob = xhist * np.diff(xedges)
    y_prob = yhist * np.diff(yedges)
    kl_avg = (kl_divergence(x_prob,y_prob) + kl_divergence(y_prob,x_prob))/2

    return kl_avg


def actual_feature(key,data):
    if key == 'In6_chi2':
        x_data = np.concatenate(data)[:,dica[key]]*180/np.pi
    else:
        x_data = np.concatenate(data)[:,dica[key]]*10

    return x_data

if __name__=='__main__':
    active_holo = pickle.load(open('CB2_holo_active_features.pkl','rb'))

    inactive_holo = pickle.load(open('CB2_holo_inactive_features.pkl','rb'))

    apo = pickle.load(open('CB2_apo_features.pkl','rb'))

    dica = {'Helix2M_Nloop':0, 'Ex16_distance':1,'TG_diff_z':2,'In6_chi2':3,'In57_distance':4,'In52_distance':5,'In36_distance':6}

    keys = ['Helix2M_Nloop', 'Ex16_distance','TG_diff_z','In6_chi2','In57_distance','In52_distance','In36_distance']
    
    x_lim = {'Helix2M_Nloop':[15,45],'Ex16_distance': [15,40],'TG_diff_z':[-8,8],'In6_chi2':[-180,180],'In57_distance':[5,22],'In52_distance':[7,22],'In36_distance':[6,20]}

    y_lim = {'Helix2M_Nloop':[0,1.2],'Ex16_distance': [0,0.8],'TG_diff_z':[0,1.2],'In6_chi2':[0,0.05],'In57_distance':[0,1.0],'In52_distance':[0,0.8],'In36_distance':[0,0.8]}

    x_label = {'Helix2M_Nloop':'N terminus movement ', 'Ex16_distance': 'TM1 movement ','TG_diff_z':'Toggle Switch translation ' ,'In6_chi2': 'Toggle Switch rotation ','In57_distance':'TM7 movement ','In52_distance':'TM5 movement ','In36_distance': 'TM6 movement '}

    print(' Feature  Mean Diff.  K-L div(Active)  K-L div(Inactive) ')
    for key in keys:
        active_holo_data = actual_feature(key,active_holo)
        inactive_holo_data = actual_feature(key,inactive_holo)
        apo_data = actual_feature(key,apo)

        minimum = min([np.min(active_holo_data),np.min(inactive_holo_data),np.min(apo_data)])
        maximum = max([np.max(active_holo_data),np.max(inactive_holo_data),np.max(apo_data)])
        
        active_holo_data_norm = (active_holo_data - minimum)/(maximum-minimum)
        inactive_holo_data_norm = (inactive_holo_data - minimum)/(maximum-minimum)
        apo_data_norm = (apo_data - minimum)/(maximum-minimum)
        
        kl_div_active = kl_calculation(active_holo_data_norm,apo_data_norm)
        kl_div_inactive = kl_calculation(inactive_holo_data_norm,apo_data_norm)
        
        print(x_label[key], np.round(np.abs(np.mean(active_holo_data_norm) - np.mean(apo_data_norm)) + np.abs(np.mean(inactive_holo_data_norm) - np.mean(apo_data_norm)),1), np.round(kl_div_active,1), np.round(kl_div_inactive,1))
