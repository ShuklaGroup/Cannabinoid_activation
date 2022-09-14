import numpy as np 
import glob 
import matplotlib.pyplot as plt 
from matplotlib import rc
hfont = {'fontname':'Helvetica'}
rc('text', usetex=True)
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})


def rgb_to_hex(r, g, b):
    return ('#{:02X}{:02X}{:02X}').format(r, g, b)

def line_plot(array_dict,matrics):
    fig,axs = plt.subplots(1,1)
    values = list(array_dict.values())
    pdbs = list(array_dict.keys())
    xmin = axis_lim[matrics][0]
    xmax = axis_lim[matrics][1]
    y = 5
    height = 0.01
    axs.set_xlim(xmin,xmax)
    plt.hlines(y, xmin, xmax)
    plt.vlines(xmin, y - height / 2., y + height / 2.)
    plt.vlines(xmax, y - height / 2., y + height / 2.)
    for value,pdb in zip(values,pdbs):
        plt.plot(value,y, marker_dict[pdb_dict[pdb][0]], ms = 15, mfc = color_dict[pdb_dict[pdb][1]])
    plt.axis('off')
    if matrics != 'TG_rota':
        plt.text(xmin - 0.05, y, str(xmin) + '\AA' , horizontalalignment='right',**hfont,fontsize=22)
        plt.text(xmax + 0.05, y, str(xmax) + '\AA', horizontalalignment='left',**hfont,fontsize=22)
    else:
        plt.text(xmin - 0.05, y, str(xmin) + '$^\circ$' , horizontalalignment='right',**hfont,fontsize=22)
        plt.text(xmax + 0.05, y, str(xmax) + '$^\circ$', horizontalalignment='left',**hfont,fontsize=22)

    plt.savefig('CB1_' + matrics,dpi=500)
    plt.close()




if __name__=='__main__':

    color_dict = {'active':rgb_to_hex(int(255*0.02), int(255*0.38), int(255*0.67)),'inactive':'orange'}

    marker_dict = {'agonist':'v','antagonist':'o','agonist_Gi':'s','agonist_nam':'*'}

    pdb_dict = {'5xr8':['agonist','active'],'5xra':['agonist','active'],'7v3z':['agonist','active'],'6n4b':['agonist_Gi','active'],'6kpg':['agonist_Gi','active'],'5tgz':['antagonist','inactive'],'5u09':['antagonist','inactive'],'6kqi':['agonist_nam','inactive']}

    plot_dict = {'Nloop':['5xr8','7v3z','5tgz','5u09','6kqi'],'TM1_movement':['5xr8','5xra','7v3z','5tgz','5u09','6kqi','6n4b','6kpg'],'TM6_movement':['5xr8','5xra','7v3z','5tgz','5u09','6kqi','6n4b','6kpg'],'npxxy':['5xr8','5xra','7v3z','5tgz','5u09','6kqi','6n4b','6kpg'],'TM5_movement':['5xr8','5xra','7v3z','5tgz','5u09','6kqi','6n4b','6kpg'],'TG_rota':['5xr8','5xra','7v3z','5tgz','5u09','6kqi','6n4b','6kpg'],'TG_diff_z':['5xr8','5xra','7v3z','5tgz','5u09','6kqi','6n4b','6kpg']}

    arr_pos = {'Nloop':-7,'TM1_movement':-6, 'TG_rota':-5, 'TG_diff_z':-4, 'TM5_movement':-3, 'TM6_movement':-2,'npxxy':-1}

    axis_lim = {'Nloop':[16,34],'TM1_movement':[20,30],'TM6_movement':[9,17],'npxxy':[6,18], 'TM5_movement':[7,17],'TG_rota':[20,120],'TG_diff_z':[-8,6]}


    for matrics in list(plot_dict.keys()):
        array_dict = {}
        for pdb in plot_dict[matrics]:
            filename = './CB1_' + pdb_dict[pdb][0] + '_' + pdb_dict[pdb][1] + '_' + pdb + '.npy'
            if matrics == 'TG_rota':
                array_dict[pdb] = np.load(filename)[arr_pos[matrics]]*180/np.pi
            else:
                array_dict[pdb] = np.load(filename)[arr_pos[matrics]]*10

        line_plot(array_dict,matrics)




    
