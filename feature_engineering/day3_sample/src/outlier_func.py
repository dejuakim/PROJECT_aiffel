
def outlier_func(dating_df):
    o_score = []
    i_score = []
    
    for i in dating_df.columns:
        if i.startswith('o_score'):
            o_score.append(i)
        elif i.startswith('i_score'):
            i_score.append(i)
    
    for i in o_score:
        dating_df[i] = dating_df[i].apply(lambda x: 10  if x > 10  else x )
    
    for i in i_score:
        dating_df[i] = dating_df[i].apply(lambda x: 10  if x > 10  else x )
    
    return dating_df
