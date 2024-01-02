import pandas as pd
import os
from tkinter import Tk, filedialog
from get_folder_path import get_folder_path

#define column names

def import_data_from_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    print(folder_name)

    # Get all files in the selected directory
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    normalized_data_columns = ['E_E_VBM', 'raw_data']
    fit_columns = ['E_E_VBM', 'fit']
    unconvolved_dos_columns = ['E_E_VBM', 'unconv_dos']
    vbm_edge_dos_plog_columns = ['E_E_VBM', 'vbm_plog']
    vb2_main_dos_plog_columns = ['E_E_VBM', 'vb2_plog']
    extra_matrix_columns = ['E_E_VBM', 'VB_conv_transfer_function', 'Def1', 'Def2', 'Def3', 'Def4', 'DefSum_WithoutVB', 'Data_WithoutDefecs', 'residuals']


    # Define dictonary for index renaming
    column_name_rules = {
        'Fitting paremeters': None,
        'Normalized data': normalized_data_columns,
        'Fit': fit_columns,
        'Unconvolved DOS':  unconvolved_dos_columns,
        'VB edge':  vbm_edge_dos_plog_columns,
        'Main VB': vb2_main_dos_plog_columns,
        'Extra':  extra_matrix_columns 
    }

    # Define file patterns
    file_patterns = {
        'Fitting paremeters': 'Fitting paremeters',
        'Normalized data': 'Normalized data',
        'Fit': 'Fit',
        'Unconvolved DOS': 'Unconvolved DOS',
        'VB edge': 'VB edge',
        'Main VB': 'Main VB',
        'Extra': '[Extra]'
    }

    # Initialize dictionaries for dataframes
    dataframes = {key: None for key in file_patterns}

    for key, pattern in file_patterns.items():
        matching_files = [f for f in all_files if pattern in f]

        if matching_files:
            # If key is 'Fit,' ensure that 'Fitting paremeters' is not considered
            if key == 'Fit':
                matching_files = [f for f in matching_files if 'Fitting paremeters' not in f and 'graph' not in f]

            file_path = os.path.join(folder_path, matching_files[0])

            # Use the predefined column names for each key
            columns = column_name_rules.get(key, None)
            
            # Read the CSV file with specified columns and no header
            df = pd.read_csv(file_path, names=columns, header=None, sep='\t')

            dataframes[key] = df
        else:
            print(f"Warning: {key} file not found in the folder.")

    # Return dataframes
    return dataframes