import matplotlib.pyplot as plt
from get_folder_path import get_folder_path
from import_data_from_folder import import_data_from_folder
from PES_figure_settings import PES_figure_settings
import numpy as np
import os

# Call the function to select the folder path in gui
folder_path = get_folder_path()

# Or provide the folder path here
# folder_path = '/Users/dorotheemenzel/Documents/Coding/example_data/01_ProperFit_20231130'

# Print the path to check that the right one was selected
# print(f"Selected folder path: {folder_path}")
dataframes = import_data_from_folder(folder_path)

# Access individual dataframes
fitting_parameters = dataframes['Fitting paremeters']
normalized_data = dataframes['Normalized data']
fit = dataframes['Fit']
unconvolved_dos = dataframes['Unconvolved DOS']
vbm_edge_dos_plog = dataframes['VB edge']
vb_main_edge_dos_plog = dataframes['Main VB']
extra_matrix = dataframes['Extra']


E_vbm_min = -1
E_vbm_max = 3
energy_stepsize = 0.5
IY_Min = 10**(-7)
IY_Max = 10**(1)


# Import figure settings
figsize_normal = PES_figure_settings['figsize_normal']
fontsize_label = PES_figure_settings['fontsize_label']
fontsize_axlabel = PES_figure_settings['fontsize_axlabel']
linewidth_thin = PES_figure_settings['linewidth_thin']
linewidth_medium = PES_figure_settings['linewidth_medium']
linewidth_thick = PES_figure_settings['linewidth_thick']

# Create figure ready for subplots
fig, ax1 = plt.subplots(figsize = figsize_normal)

# Both Datasets in same axes
fit_result_plot = ax1.plot(
   normalized_data.E_E_VBM, normalized_data.raw_data, 'o', label='raw data', 
    color = 'grey', linewidth = linewidth_medium)
fit_result_plot = ax1.plot(
   fit.E_E_VBM, fit.fit, '-', label='fit', 
    color = 'red', linewidth = linewidth_medium)
fit_result_plot = ax1.plot(
   unconvolved_dos.E_E_VBM, unconvolved_dos.unconv_dos, '-', label='unconvolved DOS', 
    color = 'black', linewidth = linewidth_medium)
fit_result_plot = ax1.plot(
   vbm_edge_dos_plog.E_E_VBM, vbm_edge_dos_plog.vbm_plog, '-', label='VBM', 
    color = 'blue', linewidth = linewidth_medium)

fit_result_plot = ax1.plot(
   extra_matrix.E_E_VBM, extra_matrix.Def1, '-', label='Def1', 
    color = 'orange', linewidth = linewidth_thin)
fit_result_plot = ax1.plot(
   extra_matrix.E_E_VBM, extra_matrix.Def2, '-', label='Def2', 
    color = 'orange',  linewidth = linewidth_thin)
fit_result_plot = ax1.plot(
   extra_matrix.E_E_VBM, extra_matrix.Def3, '-', label='Def3', 
    color = 'orange', linewidth = linewidth_thin)
fit_result_plot = ax1.plot(
   extra_matrix.E_E_VBM, extra_matrix.Def4, '-', label='Def4', 
    color = 'orange',  linewidth = linewidth_thin)

#Settings concerning both axes
ax1.set_xlabel('E-E$_{VBM}$ [eV]', fontsize = fontsize_axlabel)
ax1.set_xticks(np.arange(E_vbm_min,E_vbm_max,energy_stepsize))

# Set Internal Yield axes
ax1.set_yscale('log')
ax1.set_ylabel('Internal Yield [eV$^{-1}$s$^{-1}$]', fontsize = fontsize_axlabel)
ax1.set_ylim([IY_Min, IY_Max])

plt.savefig(os.path.join(folder_path, 'graph_CFSYS_Fit_results_log.png'))

plt.show()

