# Purpose:  Extract medication/dosage info, check for potential spelling issues.
# Version:  1
# Author:   Luzia Troebinger
# Status:   Closed
# Created:  14-Dec-2021

import re
from difflib import SequenceMatcher

def my_meds_reader_close_matches(s):
    """ 
    Reads data from text file and returns medication name.
    Returns similarity score for non-matching drug names.

    Parameters
    ----------
    s:  str
        input string
    
    Returns
    -------
    meds_dose_list: list
        list of lists containing medication code (int) and dose (str) (e.g. [[1,'75mg daily'],[3,'100mg every 2 hours']])
    Names of non-matched drugs
    Match ratio comparing non-matches to each drug searched for
    """
    # names of drugs to search in text
    meds_to_search = {'aspirin': 2, 'paracetamol': 1,'panadol': 1,'penicillin': 3}

    # split on empty line\line containing only whitespaces.
    # retain string content prior to first split only
    s = re.split("\n\s*\n",s.lstrip())[0]

    # lower case everything
    s = s.lower()

    # split into individual lines
    s = s.split('\n')

    # split on first whitespace
    s_split = [f.split(" ",1) for f in s]

    # get non matches
    non_matched_only = [f[0] for f in s_split
                        if f[0] not in meds_to_search.keys()]

    # check whether non matches are a close match for any of the drugs
    match_ratio = [[f, key, SequenceMatcher(None,f,key).ratio()]
                    for f in non_matched_only 
                    for key in meds_to_search.keys()]
    
    #check for highest match ratio in each sublist
    similarity = []
    for name in non_matched_only:  
        max_match = max([f for f in match_ratio if name in f], key=lambda item: item[2])
        similarity.append(max_match)
    print(f'For non-matching drug names, the highest similarity was: {similarity}')

    # replace medication names with key (str)]
    meds_dose_list=[[meds_to_search[f[0]],f[1]]
                    if len(f)>1 else 
                    [meds_to_search[f[0]],""]
                    for f in s_split
                    if f[0] in meds_to_search.keys()]
    
    return meds_dose_list, non_matched_only, match_ratio