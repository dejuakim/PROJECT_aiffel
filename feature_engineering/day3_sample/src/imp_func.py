
def imp_func(dating_df):
    o_imp = []

    for i in dating_df.columns:
        if i.startswith('o_important'):
            o_imp.append(i)
            
    dating_df['o_imp_sum'] = dating_df[o_imp].sum(axis = 1)
    
    i_imp = []

    for i in dating_df.columns:
        if i.startswith('i_important'):
            i_imp.append(i)
            
    dating_df['i_imp_sum'] = dating_df[i_imp].sum(axis = 1)
    
    dating_df[o_imp] = dating_df.apply(lambda x: (100 / x['o_imp_sum']) * x[o_imp], axis = 1)
    dating_df[i_imp] = dating_df.apply(lambda x: (100 / x['i_imp_sum']) * x[i_imp], axis = 1)
    dating_df.drop(['o_imp_sum','i_imp_sum'], axis=1, inplace = True)
    
    return dating_df
