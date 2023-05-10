def is_pair_solved(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] == 'o' or s2[i] == 'o':
            continue
        else:
            return False
    return True
