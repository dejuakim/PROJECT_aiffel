
import sys

sys.path.append('./src')

import pandas as pd
import numpy as np
from col_rename import col_rename
from missing_func import missing_func
from outlier_func import outlier_func
from imp_func import imp_func
from age_gap_func import age_gap_func
from race_func import race_func
from rating_func import rating_func
from sel_one_func import sel_one_func

def pre_func(dating_df):
    dating_df = col_rename(dating_df)
    dating_df = missing_func(dating_df)
    dating_df= outlier_func(dating_df)
    dating_df = imp_func(dating_df)
    dating_df = age_gap_func(dating_df)
    dating_df = race_func(dating_df)
    dating_df = rating_func(dating_df)
    dating_df = sel_one_func(dating_df)
    
    return dating_df
    
