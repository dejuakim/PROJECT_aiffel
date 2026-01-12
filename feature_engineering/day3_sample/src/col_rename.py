
def col_rename(dating_df):
    new_cols = []

    for i in dating_df.columns:
        if i.startswith('pref_o'):
            i = i.replace('pref_o', 'o_important')
        elif i.endswith('_o'):
            i = 'o_score_' + i.replace('_o', '')
        elif i.endswith('_important'):
            i = 'i_important_' + i.replace('_important', '')
        elif i.endswith('_partner'):
            i = 'i_score_' + i.replace('_partner', '')
        new_cols.append(i)
    dating_df.columns = new_cols
    dating_df = dating_df.rename({'o_score_race': 'race_o', 'o_score_age': 'age_o'}, axis = 1)
    
    return dating_df
