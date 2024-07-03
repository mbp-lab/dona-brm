#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:01:04 2024

@author: olya
"""

def save_variables(filepath,key,value):
    """
    Saves the given values in a file for future reference, e.g. to have an easy access
    when writing papers and for updating paper numbers automatically based on the values from
    the resulting output file. 
    
    Parameters
    ----------
    filepath : str
             where to store the variable values
    key: str
            an identifier
    value: any-type
           the target value

    Returns
    -------
    """

    import csv
    import numpy as np
    dict_var = {}
    try:
        with open(filepath, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                dict_var[row[0]] = row[1]
    except:
        pass
    try:
        dict_var[key] = np.round(value,2)
    except:
        dict_var[key] = value
    
    with open(filepath, "w") as f:
        for key in dict_var.keys():
            f.write(f"{key},{dict_var[key]}\n")


    
def save_descriptive_stats(filepath,key,data):
    """
    Calculates the descriptive statistics of a given variable and saves them in a file
    
    Parameters
    ----------
    filepath : str
             where to store the variable values
    key: str
            an identifier
    value: any-type
           the target value

    Returns
    -------
    """

    import numpy as np
    from scipy.stats import median_abs_deviation as mad
    save_variables(filepath,f'{key}-N',sum(~np.isnan(data)))
    save_variables(filepath,f'{key}-mean',np.nanmean(data))
    save_variables(filepath,f'{key}-median',np.nanmedian(data))
    save_variables(filepath,f'{key}-std',np.nanstd(data))
    save_variables(filepath,f'{key}-mad',mad(data,nan_policy='omit'))
    save_variables(filepath,f'{key}-min',min(data))
    save_variables(filepath,f'{key}-max',max(data))

def set_aspect(ax):

    x0,x1 = ax.get_xlim()
    y0,y1 = ax.get_ylim()
    ax.set_aspect(abs(x1-x0)/abs(y1-y0))



