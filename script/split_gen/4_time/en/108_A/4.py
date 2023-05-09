def num_of_ways_to_choose_a_pair(k):
    if k % 2 == 0:
        return (k//2)**2
    else:
        return ((k-1)//2)*((k+1)//2)
