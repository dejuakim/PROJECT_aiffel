
def missing_func(dating_df):
    drop_cols = []

    for i in dating_df.columns:
        if i.startswith('o_important'):
            drop_cols.append(i)
        elif i.startswith('i_important'):
            drop_cols.append(i)
            
    dating_df = dating_df.dropna(subset = drop_cols)
    dating_df = dating_df.fillna(-99)
    
    return dating_df
