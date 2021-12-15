# Purpose:  Extract medication/dosage info.
# Version:  1
# Author:   Luzia Troebinger
# Status:   Closed
# Created:  13-Dec-2021

import re

def my_meds_reader(s):
    """ 
    Replaces names of pre-specified list of meds with int values.

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
    # meds to replace and values to replace them with
    meds_to_search = {'aspirin': 2, 'paracetamol': 1,
                        'panadol': 1,'penicillin': 3}
    
    # just in case, remove leading white space
    # otherwise a blank line at the start could break this.
    s = s.lstrip()
    # split on blank line
    # may or may not contain whitespace
    # retain first block only
    s = re.split("\n\s*\n",s)[0]
    s = s.lower()

    # each drug on a separate line
    s = s.split('\n')

    # create list of lists
    # format: [['drug','dosage']]
    s_split = [f.split(" ",1) for f in s]

    # replace medication names (str) with key (int)
    meds_dose_list=[[meds_to_search[f[0]],f[1]]
                    if len(f)>1 else 
                    [meds_to_search[f[0]],""]
                    for f in s_split
                    if f[0] in meds_to_search.keys()]
    
    return meds_dose_list