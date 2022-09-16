import numpy as np 
import pickle
import scipy.stats
import pyemma
import sys

def micro_to_macro(cluster_number,assignments,dtrajs_com):
    cluster_macro_index = np.zeros([cluster_number,6])
    counts = [(assignments == i).sum() for i in range(6)]
    for i in range(cluster_number):
        s = assignments[np.where(dtrajs_com==i)[0]]
        unique_s = np.unique(s)
        for element in unique_s:
            cluster_macro_index[i,element] = (s==element).sum()/counts[element]
    
    micro_to_macro = cluster_macro_index.argmax(1)
    new_states = []
    for i in range(6):
        new_states.append(np.where(micro_to_macro==i)[0])

    return new_states 


def custer_numbering(missing_clusters,cluster):
    count = 0
    if len(missing_clusters) > 0:
        for i in range(len(missing_clusters)+1):
            if cluster < missing_clusters[i]:
                new_cluster = cluster - count
                break 
            else:
                count = count + 1
                if count == len(missing_clusters):
                    new_cluster = cluster - count 
                    break

    else:
        new_cluster = cluster 
    return new_cluster


if __name__ == "__main__":
    cluster_number = 400

    labels = ['I3','I1','Inactive','I2','I3','Active','I4']
    state_prob = pickle.load(open('./CB1_state_prob.pkl','rb'))
    state_prob_com = np.concatenate(state_prob)

    assignments = state_prob_com.argmax(1)

    file = './CB1_msm_feature_final_clustering.pkl'

    dtrajs_ref = pickle.load(open(file,'rb'))
    dtrajs_com = np.concatenate(dtrajs_ref)

    new_states = micro_to_macro(cluster_number,assignments,dtrajs_com)

    MFPT_CB1 = np.zeros([6,6,200])

    for k in range(200):
        msm = pickle.load(open("../Bootstrap_files/CB1_bt_80_" + str(k) +"_msm.pkl",'rb'))
        active_set = set(msm.active_set)
        cluster_set = set([i for i in range(cluster_number)])
        missing_clusters =  sorted(list(cluster_set - active_set))
        
        macro_to_micro_list = [[],[],[],[],[],[]]
        for i in range(6):
            for j in new_states[i]:
                if j not in missing_clusters:
                    macro_to_micro_list[i].append(custer_numbering(missing_clusters,j))

        for i in range(6):
            for j in range(6):
                if i == j:
                    continue
                else:
                    fc = list(macro_to_micro_list[i])
                    sc = list(macro_to_micro_list[j])
                    if not (len(fc) == 0 or len(sc) == 0):
                        tpt = pyemma.msm.tpt(msm,fc,sc)
                    MFPT_CB1[i,j,k] = tpt.mfpt/10000
    
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            else:
                mean = np.mean(MFPT_CB1[i,j,:])
                std = np.std(MFPT_CB1[i,j,:])
                print(labels[i] + ' --> ' + labels[j] + ' :' + ' ' +  str(mean) + ' +/- ' + str(std))
                #print(MFPT_CB1[i,j,:])
    
    np.save('./CB1_vampnet_states_mfpt.npy',MFPT_CB1)

