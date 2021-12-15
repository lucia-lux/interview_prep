# interview_prep
Interview task for Senior Research Fellow position (14/12/2021).
Brief in folder.

Files as follows:
my_meds_reader.py - main interview task, see description in folder
my_meds_reader_w_keys.py - accept additional input (task 2)
my_meds_reader_close_matches.py - check how close non-matches are to drug names we are searching for (task 3)
medfunc.ipynb - scrapbook I used for trying out different options
final_funcs.ipynb - has all three 'final' functions in a single notebook, which I used for my presentation.

Main task (1):
Added an .lstrip() before separating on first blank line to cover for the case where the document might start with a blank line.
Wasn't specified in the brief but I couldn't help myself (only added after interview).

Task 3:
My initial thoughts were to use Levenshtein distance to search for and then replace close matches with 'correct' drug names.
In the end, I didn't go for this because the brief did not really clarify where this would sit within a larger module.
Just replacing seemed a bit of a risky choice, so I just went for a function that returns the 'searched for' drug name that has the most overlap with a given non-match.
Solutions is based on difflib/SequenceMatcher()

Test case in the folder.
No additional test cases in interview.
