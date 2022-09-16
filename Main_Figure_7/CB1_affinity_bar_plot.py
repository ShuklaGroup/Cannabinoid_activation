import numpy as np 
import glob 
import matplotlib.pyplot as plt 
from matplotlib import rc
import pickle

hfont = {'fontname':'Helvetica','fontweight':'bold'}
rc('text', usetex=True)
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

def rgb_to_hex(r, g, b):
    return ('#{:02X}{:02X}{:02X}').format(r, g, b)


if __name__=='__main__':
    states = ['2','1','3','0','5','4']
    labels = ['Inactive','I1','I2','I3','I4','Active']
    
    fig, axs = plt.subplots(1,1,figsize=(10,7))

    ligand_energy = np.zeros([4,6,100])
    for i in range(1,5):
        for j,state in enumerate(states):
            ligand_energy[i-1,j,:] = pickle.load(open('./CB1_macrostate_pdb_'+ state + '_CB2_agonist_' + str(i) + '_docking_energy.pkl','rb'))
    
    ligand_mean_energy = np.mean(ligand_energy,axis=2)
    ligand_std_energy = np.std(ligand_energy,axis=2)
    
    x = np.arange(0,15,4)
    width = 0.5
    for i in range(6):
        k = 5 - 2*i
        axs.bar(x - width*k/2, ligand_mean_energy[:,i], yerr = ligand_std_energy[:,i]/10, width= width, color = rgb_to_hex(int(255*(1.00-0.98/5*i)),int(255*(0.5-0.12/5*i)),int(255*(0.0+0.67/5*i))),align='center', alpha=0.8, ecolor='black', capsize=10)
     
    plt.ylabel('Docking Affinity (Kcal/mol)', **hfont,fontsize=24)
    axs.set_xticks(x)
    axs.set_xticklabels(['JWH-133','HU-308','JWH-015','AM1241'])
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    axs.legend(labels,fontsize=18)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('CB1_state_CB2_agonist_docking',dpi=500) 

