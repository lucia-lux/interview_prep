# Purpose:  Extract medication/dosage info, allow additional key-value pairs as input.
# Version:  1
# Author:   Luzia Troebinger
# Status:   Active
# Created:  13-Dec-2021

import re

def my_meds_reader_w_keys(s,**kwargs):
    """ 
    Replaces meds names with key (int).
    Takes additiona key-value pairs as optional args.

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
    meds_to_search = {'aspirin': 2, 'paracetamol': 1,'panadol': 1,'penicillin': 3}
 
    # if keyword args supplied, add key/value pairs
    if kwargs:
        for new_entries in kwargs.values():
            # names of drugs to search in text
            meds_to_search.update(new_entries)
    

    # split on empty line\line containing only whitespaces.
    # retain string content prior to first split only (ignore anything below \n\s*\n)
    s = re.split("\n\s*\n",s)[0]

    # lower case everything
    s = s.lower()

    # split into individual lines
    s = s.split('\n')

    # split on first whitespace
    s_split = [f.split(" ",1) for f in s]

    # replace medication names with key (str)]
    meds_dose_list=[[meds_to_search[f[0]],f[1]]
                    if len(f)>1 else 
                    [meds_to_search[f[0]],""]
                    for f in s_split
                    if f[0] in meds_to_search.keys()]
    
    return meds_dose_list