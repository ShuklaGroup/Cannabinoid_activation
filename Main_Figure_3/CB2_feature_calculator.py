import glob 
import mdtraj as md 
import numpy as np

for filename in glob.glob('./CB2*.pdb'):
    t = md.load(filename)
    filename =  filename.split('.pdb')[0]
    helix1E = t.topology.select('name CA and residue 32')
    helix6E = t.topology.select('name CA and residue 268')
    Nloop = t.topology.select('name CA and residue 25')
    helix2I = t.topology.select('name OH and residue 70')
    helix7I = t.topology.select('name OH and residue 299')
    helix3I = t.topology.select('name CA and residue 131')
    helix6I = t.topology.select('name CA and residue 245')
    helix5I = t.topology.select('name CA and residue 205')
    TRP_NE = t.topology.select('name NE1 and residue 258')
    helix2MI = t.topology.select('name CA and residue 80')
    TRP_CA = t.topology.select('name CA and residue 258')
    TRP_CB = t.topology.select('name CB and residue 258')
    TRP_CG = t.topology.select('name CG and residue 258')
    TRP_CD = t.topology.select('name CD1 and residue 258')
    TYR_OH = t.topology.select('name OH and residue 209')
    ILE_CA = t.topology.select('name CA and residue 73')
    TG_trp_sidechain = t.topology.select('sidechain and residue 258')
    TG_phe_sidechain = t.topology.select('sidechain and residue 117')
    distI = np.empty(7)
    distI[:2] = md.compute_distances(t,[[Nloop[0],helix2MI[0]],[helix1E[0],helix6E[0]]],periodic=False)
    atom_index,angle = md.compute_chi2(t, periodic=False)
    trp_index = np.where(atom_index==[TRP_CA[0],TRP_CB[0],TRP_CG[0],TRP_CD[0]])
    distI[2] = angle[:,trp_index[0][0]]
    distI[3] = np.mean(t.xyz[:,TG_trp_sidechain,2],axis=1) - np.mean(t.xyz[:,TG_phe_sidechain,2],axis=1)
    distI[4:] = md.compute_distances(t,[[helix5I[0],helix7I[0]],[helix3I[0],helix6I[0]],[TYR_OH[0],ILE_CA[0]]],periodic=False)
    np.save(filename,distI)

    print(filename,distI)

