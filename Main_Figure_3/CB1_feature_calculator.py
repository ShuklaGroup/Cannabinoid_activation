import glob 
import mdtraj as md 
import numpy as np




for filename in glob.glob('./CB1*pdb'):
    t = md.load(filename)
    print(filename)
    filename =  filename.split('.pdb')[0]
    helix1E = t.topology.select('name CA and residue ' + str(116))
    helix6E = t.topology.select('name CA and residue ' + str(366))
    Nloop = t.topology.select('name CA and residue ' + str(103))
    helix2I = t.topology.select('name OH and residue ' + str(153))
    helix5I = t.topology.select('name CA and residue ' + str(290))
    helix7I = t.topology.select('name OH and residue ' + str(397))
    helix3I = t.topology.select('name CA and residue ' + str(214))
    helix6I = t.topology.select('name CA and residue ' + str(343))
    TRP_NE = t.topology.select('name NE1 and residue 356')
    helix2MI = t.topology.select('name CA and residue ' + str(163)) 
    TRP_CA = t.topology.select('name CA and residue 356')
    TRP_CB = t.topology.select('name CB and residue 356')
    TRP_CG = t.topology.select('name CG and residue 356')
    TRP_CD = t.topology.select('name CD1 and residue 356')
    TYR_OH = t.topology.select('name OH and residue 294')
    ILE_CA = t.topology.select('name CA and residue 156')

    TG_trp_sidechain = t.topology.select('sidechain and residue 356')
    TG_phe_sidechain = t.topology.select('sidechain and residue 200')

    #print(helix1E,helix6E,Nloop,helix2I,helix7I,helix3I,helix6I,TRP_NE,helix2MI)
    dist_array = np.empty(7)
    if len(Nloop) > 0:
        dist_array = np.empty(7)
        dist_array[:2] = md.compute_distances(t,[[Nloop[0],helix2MI[0]],[helix1E[0],helix6E[0]]],periodic=False)
        atom_index,angle = md.compute_chi2(t, periodic=False)
        trp_index = np.where(atom_index==[TRP_CA[0],TRP_CB[0],TRP_CG[0],TRP_CD[0]])
        dist_array[2] = angle[:,trp_index[0][0]]
        dist_array[3] = np.mean(t.xyz[:,TG_trp_sidechain,2],axis=1) - np.mean(t.xyz[:,TG_phe_sidechain,2],axis=1)
        dist_array[4:] = md.compute_distances(t,[[helix5I[0],helix7I[0]],[helix3I[0],helix6I[0]],[TYR_OH[0],ILE_CA[0]]],periodic=False)
        np.save(filename,dist_array)
    
    else:
        dist_array = np.empty(6)
        dist_array[:1] = md.compute_distances(t,[[helix1E[0],helix6E[0]]],periodic=False)
        atom_index,angle = md.compute_chi2(t, periodic=False)
        trp_index = np.where(atom_index==[TRP_CA[0],TRP_CB[0],TRP_CG[0],TRP_CD[0]])
        dist_array[1] = angle[:,trp_index[0][0]]
        dist_array[2] = np.mean(t.xyz[:,TG_trp_sidechain,2],axis=1) - np.mean(t.xyz[:,TG_phe_sidechain,2],axis=1)
        dist_array[3:] = md.compute_distances(t,[[helix5I[0],helix7I[0]],[helix3I[0],helix6I[0]],[TYR_OH[0],ILE_CA[0]]],periodic=False)
        np.save(filename,dist_array)

