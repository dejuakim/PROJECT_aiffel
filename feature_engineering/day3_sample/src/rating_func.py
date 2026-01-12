
def rating_func(dating_df):
    
    o_important = []
    o_score = []
    i_important = []
    i_score = []

    for i in dating_df.columns:
        if i.startswith('o_important'):
            o_important.append(i)
        elif i.startswith('o_score'):
            o_score.append(i)
        elif i.startswith('i_important'):
            i_important.append(i)
        elif i.startswith('i_score'):
            i_score.append(i)
    
    dating_df[o_important] = dating_df[o_important].replace({0: -99})
    dating_df[i_important] = dating_df[i_important].replace({0: -99})
    
    def rating(data, important, score):
        if data[score] == -99:
            return -99
        elif data[important] == -99:
            return -99
        else:
            return data[important] * data[score]
        
    o_rating = ['o_rating_attractive',
     'o_rating_sincere',
     'o_rating_intellicence',
     'o_rating_funny',
     'o_rating_ambtition',
     'o_rating_shared_interests']
    
    i_rating = ['i_rating_attractive',
     'i_rating_sincere',
     'i_rating_intellicence',
     'i_rating_funny',
     'i_rating_ambtition',
     'i_rating_shared_interests']
    
    for i, j, k in zip(o_important, o_score, o_rating):
         dating_df[k] = dating_df.apply(lambda x: rating(x, i, j), axis = 1)
            
    for i, j, k in zip(i_important, i_score, i_rating):
         dating_df[k] = dating_df.apply(lambda x: rating(x, i, j), axis = 1)
    
    dating_df['o_rating_total'] = dating_df[o_rating].apply(lambda x: x[x > 0 ].mean(), axis = 1)
    dating_df['i_rating_total'] = dating_df[i_rating].apply(lambda x: x[x > 0 ].mean(), axis = 1)
    dating_df['rating_mean'] = 2 * dating_df['o_rating_total'] * dating_df['i_rating_total'] / (dating_df['o_rating_total'] + dating_df['i_rating_total'])
    
    return dating_df
