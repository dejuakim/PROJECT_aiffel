
def race_func(dating_df):
    dating_df['same_race'] = (dating_df['race'] == dating_df['race_o']).astype('int')
    dating_df['same_race'] = dating_df['same_race'].replace({0: -1})
    dating_df['same_race_point'] = dating_df['same_race'] * dating_df['importance_same_race']
    return dating_df
