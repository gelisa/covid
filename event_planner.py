def get_prob(inf_num, event_size):
    pi = inf_num / 10**6
    return 1 - (1- pi)**event_size

def get_event_size(prob, inf_num, pop_size=10**6):
    pi = inf_num / pop_size
    return np.log10(1 - prob) / np.log10(1 - pi) 
    
    
