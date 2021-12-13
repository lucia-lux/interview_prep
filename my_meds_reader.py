# Purpose:  Extract medication/dosage info.
# Version:  1
# Author:   Luzia Troebinger
# Status:   Active
# Created:  13-Dec-2021

import re

def my_meds_reader(s):
    """ 
    Reads data from text file and returns medication name.

    Parameters
    ----------
    s:  str
        input string
    
    Returns
    -------
    meds_dose_list: list
        list of lists containing medication code (int) and dose (str)
        (e.g. [[1,'75mg daily'],[3,'100mg every 2 hours']])
    """
    # names of drugs to search in text
    meds_to_search = {'aspirin': 2, 'paracetamol': 1,'panadol': 1,'penicillin': 3}
    
    # lower case everything
    s = s.lower()
    # split on empty line\line containing only whitespaces.
    # retain string content up to first split (ignore anything below \n\s*\n)
    s = re.split("\n\s*\n",s)[0]
    # split into individual lines
    s = s.split('\n')
    # split lines on first whitespace
    s_split = [f.split(" ",1) for f in s]

    # replace medication names (str) with key (int)
    meds_dose_list=[[meds_to_search[key],f[1]]
                    if len(f)>1 else 
                    [meds_to_search[key],""]
                    for f in s_split
                    for key in meds_to_search.keys()
                    if key in f]
    
    return meds_dose_list