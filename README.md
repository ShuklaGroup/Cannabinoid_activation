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

## Main_Figure_4 
- CB1_conditional_probability_difference.py: Python script to create the bar plot as shown in Figure 4A.
- CB2_conditional_probability_difference.py: Python script to create the bar plot as shown in Figure 4B.


## Main_Figure_5
- CB1-APO_vampnet_activation_feature_bar_plt.py: Python script to generate the bar plots for the structural features for every mestatable state
- CB1-APO_vampnet_states_TPT.py : Python script to calculate mean free passage time between every metastatble state
- CB1_state_prob.pkl: Pickle file contains the probabilities belonging to a certain metastable state of each frame of every trajectory. This file can be downloaded from https://uofi.box.com/s/xoiuicdpjhrohpjputgnk5ppuwlcfp35
- CB1_msm_feature_final_clustering.pkl: Pickle file contains cluster indices of each frame of every trajectory. This file can be downloaded from https://uofi.box.com/s/xoiuicdpjhrohpjputgnk5ppuwlcfp35
- CB1_ref_[_refstate_]_[_querystate_]_b.pdb : Representative PDB files for each metastable state containing K-L divergence value in the b-factor column.

## Main_Figure_6
- CB2-APO_vampnet_activation_feature_bar_plt.py: Python script to generate the bar plots for the structural features for every mestatable state
- CB2-APO_vampnet_states_TPT.py : Python script to calculate mean free passage time between every metastatble state
- CB2_state_prob.pkl: Pickle file contains the probabilities belonging to a certain metastable state of each frame of every trajectory. This file can be downloaded from https://uofi.box.com/s/nhfw2a8t8uuip68qk9s7fxi6vlaxbjhk
- CB2_msm_feature_final_clustering.pkl: Pickle file contains cluster indices of each frame of every trajectory. This file can be downloaded from https://uofi.box.com/s/nhfw2a8t8uuip68qk9s7fxi6vlaxbjhk
- CB2_ref_[_refstate_]_[_querystate_]_b.pdb : Representative PDB files for each metastable state containing K-L divergence value in the b-factor column.


## Main_Figure_7
- CB1_APO_vampnet_binding_pocket.py: Python script to generate the scatter plot for CB1 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7A.
- CB2_APO_vampnet_binding_pocket.py: Python script to generate the scatter plot for CB2 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7B.
- Volume calculations was performed on 100 structures on each metastable state. Calculated volume and N-terminus distance for each metatable state are saved in CB_macrostate[_metastable state index_]volume_cal.pkl and CB_macrostate[_metastable state index_]N-terminus_distance.pkl files. These files can be downloaded from https://uofi.box.com/s/vyakobq2zbk5xyoxqvccxngif6jzeo0z
- CB1_affinity_bar_plot.py: Python script to generate the bar plots of docking affinities of CB2 selective agonists (JWH-133, HU-308, JWH-015, AM1241) to CB1 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7C. 
- CB2_affinity_bar_plot.py: Python script to generate the bar plots of docking affinities of CB2 selective agonists (JWH-133, HU-308, JWH-015, AM1241) to CB1 metatable states (Inactive, active, I1, I2, I3, I4) as shown in the Figure 7D.
- As mentioned in the manuscript, docking of each ligand was performed on 100 structures on each metastable state. Resultant Docking Energies are saved in CB[1-2]macrostate_pdb[_metastable state index_]CB2_agonist[_lignad index_]docking_energy.pkl files. Each file contains 100 docking energies, where each energy is the mean of best three dock poses for a single structure in a metastable state. The indices of JWH-133, HU-308, JWH-015, AM1241 are 1,2,3,4 respectively. These files can be downloaded from https://uofi.box.com/s/vyakobq2zbk5xyoxqvccxngif6jzeo0z

## Main_Figure_8 
- Docked pdb structures of CB2 selective agonists (JWH-133, HU-308, JWH-015, AM1241) in CB1 (I2 and active) and CB2 (Inactive and active) metastable states. 

## Initial_Coordinates
- This directory contains all pdb and prmtop files necesary for starting MD simulation.   

## Striped trajectories
- CB1 apo activation: parameter and trajectory files can be found in the box folder: https://uofi.box.com/s/p0ivhqihimh8cr3mp4tua5gd7ygsijo8
- CB2 apo activation: parameter and trajectory files can be found in the box folder: https://uofi.box.com/s/xl7tpf345rt8tikjaidfa8rm7gy2wrpj
- CB1 holo active: parameter and trajectory files can be found in the box folder: https://uofi.box.com/s/a8dvtgmw4sjajcjbvmkbjbtfcpy9dy2i
- CB1 holo inactive: parameter and trajectory files can be found in the box folder: https://uofi.box.com/s/9khutxgdsjc7mriqktch5ifbxcda4fs7
- CB2 holo active: parameter and trajectory files can be found in the box folder: https://uofi.box.com/s/3ah3yftcs6e40tytnxgn8cw1g4fzrlir
- CB2 holo inactive: parameter and trajectory files can be found in the box folder: https://uofi.box.com/s/rkflfcts7vccr4dlw325k65cxfx9fj4s




