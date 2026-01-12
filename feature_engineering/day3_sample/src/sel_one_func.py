
import pandas as pd
def sel_one_func(dating_df):
    
    select_col = ['gender',
     'age',
     'race',
     'interests_correlate',
     'expected_happy_with_sd_people',
     'expected_num_interested_in_me',
     'like',
     'guess_prob_liked',     
     'age_gap',
     'age_gap_dir',
     'same_race_point',
     'o_rating_attractive',
     'o_rating_sincere',
     'o_rating_intellicence',
     'o_rating_funny',
     'o_rating_ambtition',
     'o_rating_shared_interests',
     'i_rating_attractive',
     'i_rating_sincere',
     'i_rating_intellicence',
     'i_rating_funny',
     'i_rating_ambtition',
     'i_rating_shared_interests',
     'o_rating_total',
     'i_rating_total',
     'rating_mean']
    
    final_df = dating_df[select_col]
    final_df = pd.get_dummies(final_df)
    
    return final_df
