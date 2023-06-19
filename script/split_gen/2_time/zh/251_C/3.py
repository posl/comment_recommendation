def get_max_score_index( n, s, t ):
    max_score = 0
    max_score_index = 0
    for i in range( 0, n ):
        if t[i] > max_score:
            max_score = t[i]
            max_score_index = i
    return max_score_index
