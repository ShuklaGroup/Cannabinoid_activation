import numpy as np 
import os 
import fnmatch 
import pickle
import sys
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt 


def dataloader(data,key):
    if key in ['In6_chi2','TG_angle_z']:
        return_data = data[:,CB2_dica[key]]*180/np.pi
    else:
        return_data = data[:,CB2_dica[key]]*10
    
    return return_data


def bt_condition_probability(feature,bt_number,state):
    totdist = []
    totdist = pickle.load(open('../Bootstrap_files/CB2_bt_80_' + str(bt_number) + '_feature.pkl','rb'))
    msm = pickle.load(open('../Bootstrap_files/CB2_bt_80_' + str(bt_number) + '_msm.pkl','rb'))
    
    txx = np.concatenate(totdist)
 
    condition_matrix = dataloader(txx,condition)
    feature_matrix = dataloader(txx,feature)

    if feature in ['Ex16_distance','In57_distance','In52_distance']:
        feature_truth_table = np.where(feature_matrix<thresolds[feature],1,0)
    else:
        feature_truth_table = np.where(feature_matrix>thresolds[feature],1,0)
    
    if state == 0:
        condition_truth_table = np.where(condition_matrix>thresolds[condition],1,0)
        mutual_truth_table = np.multiply(condition_truth_table,feature_truth_table)

    else:
        condition_truth_table = np.where(condition_matrix<thresolds[condition],1,0)
        mutual_truth_table = np.multiply(condition_truth_table,feature_truth_table)
 
    weights = np.concatenate(msm.trajectory_weights())
    conditional_probability = np.dot(mutual_truth_table,weights)/np.dot(condition_truth_table,weights)

    return conditional_probability


if __name__=='__main__':
    
    condition = 'In6_chi2'
    features = ['Ex16_distance','In52_distance','In36_distance','In57_distance']
    thresolds = {'Ex16_distance':22.5,'In6_chi2':60,'In52_distance':14,'In57_distance':12,'In36_distance':13}
    bt_numbers = 200

    CB2_dica = {'Ex16_distance':0,'In6_chi2':1,'In52_distance':2,'In36_distance':3,'In57_distance':4}
    
    fraction_condition  = np.zeros([len(features),bt_numbers,2])
    
    x_label = {'Helix2M_Nloop':'N terminus movement', 'Ex16_distance': 'TM1 movement ','TG_diff_z':'TG translation ' ,'In6_chi2': 'TG rotation','In57_distance':'TM7 movement','In52_distance':'TM5 movement','In36_distance': 'TM6 movement'}
    
    for i,feature in enumerate(features):
        for j in range(bt_numbers):
            for k in range(2):
                fraction_condition[i,j,k] = bt_condition_probability(feature,j,k) 
    
    pickle.dump(fraction_condition,open('./CB2_'+condition+'.pkl','wb'))
