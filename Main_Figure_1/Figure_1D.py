import numpy as np
import glob
import matplotlib.pyplot as plt
from matplotlib import rc

hfont = {'fontname':'Helvetica'}
rc('text', usetex=True)
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

def rgb_to_hex(r, g, b):
    return ('#{:02X}{:02X}{:02X}').format(r, g, b)


def volume_calculation(filename):
    f = open(filename,'r')
    data = f.readlines()
    for line in data:
        if len(line) > 0:
            if line[0] == '1':
                words = line.split('|')

    return float(words[1])


def scatter_plot(array_dict):
    fig, axs = plt.subplots(1,1,figsize=(10,7))

    for i,pdb in enumerate(list(pdb_dict.keys())):
        print(pdb)
        axs.plot(i+1,array_dict[pdb], marker_dict[pdb_dict[pdb][0]], ms = 20, mfc = color_dict[pdb_dict[pdb][1]], mec = color_dict[pdb_dict[pdb][1]])
        axs.annotate(pdb, (i+0.6, array_dict[pdb]),fontsize=22)

    plt.xlabel('CB2 Experimental Structures ',**hfont,fontsize=24)
    plt.ylabel('Binding Volume ($\AA^3$)',**hfont,fontsize=24)
    
    axs.set_yticks(range(int(50),int(210)+1,40))
    axs.set_yticklabels(range(int(50),int(210)+1,40))

    plt.xlim([0,5])
    plt.ylim([50,210])
    plt.xticks([]) 
    plt.yticks(fontsize=22)
    plt.tight_layout()
    plt.savefig('CB2_volume',transparent=False,dpi =500)





if __name__=='__main__':
    color_dict = {'active':rgb_to_hex(int(255*0.90), int(255*0.0), int(255*0.38)),'inactive':'green'}  #colors to represent active and inactive structures

    marker_dict = {'agonist':'v','antagonist':'o','agonist_Gi':'s','agonist_nam':'*'} #marker to represent bound ligand and downstream proteins

    pdb_dict = {'5zty':['antagonist','inactive'],'6pt0':['agonist_Gi','active'],'6kpf':['agonist_Gi','active'],'6kpc':['agonist','inactive']}

    array_dict = {}

    for pdb in list(pdb_dict.keys()):
        filename = '../../pdb_folder/pb_analysis/POVME_run/CB2_' + pdb_dict[pdb][0] + '_' + pdb_dict[pdb][1] + '_' + pdb + '_output.txt' #file containing the volume output based on POVME calculations
        volume = volume_calculation(filename) #function to read the volume output file
        array_dict[pdb] = volume 
        
    scatter_plot(array_dict) #scatter plot


