
def age_gap_func(dating_df):
    def age_func(x):
        if x['age'] == -99:
            return -99
        elif x['age_o'] == -99:
            return -99
        elif x['gender'] == 'female':
            return x['age_o'] - x['age']
        else:
            return x['age'] - x['age_o']
        
    dating_df['age_gap'] = dating_df.apply(age_func, axis = 1)
    dating_df['age_gap_dir'] = dating_df['age_gap'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'zero')
    dating_df['age_gap'] = abs(dating_df['age_gap'])
    
    return dating_df
