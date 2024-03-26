#!/usr/bin/python3
"""
Created on Wed Mar 13 22:45:58 2024

@author: maxwellshih1
"""
import sys
import pandas as pd
# from pandas import DataFrame

# sm_ddp.py = sys.argv[0]
SM_FILENAME = sys.argv[1]
NUM_SAM = sys.argv[2]
# print(SM_FILENAME)
# print(NUM_SAM**3 )
sm_tab=pd.read_csv(f"{SM_FILENAME}")
sm_tab['null_score']=sm_tab.isnull().sum(axis=1, numeric_only=False)
grp_sm_tab=(sm_tab.sort_values(['SampleStudy:Name','null_score']).drop_duplicates(subset='SampleStudy:Name',keep='first'))
if len(grp_sm_tab)==NUM_SAM:
    grp_sm_tab.to_csv(print("ddp_",SM_FILENAME),index=False,na_re='N/A')
    print("Congrats. sm_ddp has successfully dedup the Sample Monitor output to {NUM_SUM} rows.")
else:
    grp_sm_tab.to_csv(print("ddp_",SM_FILENAME),index=False,na_re='N/A')
    print("sm_ddp failed to deduplicate the output \n")
