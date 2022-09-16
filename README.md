#  Difference in Activation Mechanisms of Cannabinoid Receptors Regulates their Ligand Selectivity
This repository contains MSM feature file, final MSM object, codes and pdb structure files, and bootstrap samples used to genarate figures and
calculations in the manuscript.

## Main_Figure_3 
- CB1_feature_calculator.py: Python script to calculate the feature values for the conserved and unconserved features of CB1 pdb files
- CB2_feature_calculator.py: Python script to calculate the feature values for the conserved and unconserved features of CB2 pdb files  
- CB1_scatter_plot_maker.py: Python script to generate 1-D scatter plots to project the conserved and unconserved features of CB1
- CB2_scatter_plot_maker.py: Python script to generate 1-D scatter plots to project the conserved and unconserved features of CB2
- Separate Numpy files containing conserved and unserved feature values for different PDBs
- Experimentally determined PDB files in different conformational state




## Main_Figure_7
- CB1_APO_vampnet_binding_pocket.py: Python script to generate the scatter plot for CB1 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7A.
- CB2_APO_vampnet_binding_pocket.py: Python script to generate the scatter plot for CB2 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7B.
- Volume calculations was performed on 100 structures on each metastable state. Calculated volume and N-terminus distance for each metatable state are saved in CB_macrostate[_metastable state index_]volume_cal.pkl and CB_macrostate[_metastable state index_]N-terminus_distance.pkl files. These files can be downloaded from https://uofi.box.com/s/vyakobq2zbk5xyoxqvccxngif6jzeo0z
- CB1_affinity_bar_plot.py: Python script to generate the bar plots of docking affinities of CB2 selective agonists (JWH-133, HU-308, JWH-015, AM1241) to CB1 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7C. 
- CB2_affinity_bar_plot.py: Python script to generate the bar plots of docking affinities of CB2 selective agonists (JWH-133, HU-308, JWH-015, AM1241) to CB1 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7D.
- As mentioned in the manuscript, docking of each ligand was performed on 100 structures on each metastable state. Resultant Docking Energies are saved in CB[1-2]macrostate_pdb[_metastable state index_]CB2_agonist[_lignad index_]docking_energy.pkl files. Each file contains 100 docking energies, where each energy is the mean of best three dock poses for a single structure in a metastable state. The indices of JWH-133, HU-308, JWH-015, AM1241 are 1,2,3,4 respectively. These files can be downloaded from https://uofi.box.com/s/vyakobq2zbk5xyoxqvccxngif6jzeo0z

## Main_Figure_8 
- Docked pdb structures of CB2 selective agonists (JWH-133, HU-308, JWH-015, AM1241) in CB1 (I2 and active) and CB2 (Inactive and active) metastable states. 





