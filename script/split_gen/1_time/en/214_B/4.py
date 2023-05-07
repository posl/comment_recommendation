def get_num_of_triples(S,T):
    count = 0
    for a in range(0,S+1):
        for b in range(0,S+1):
            for c in range(0,S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    return count
