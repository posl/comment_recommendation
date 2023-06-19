def max_score_index(score_list):
    max_index = 0
    max_score = 0
    for i in range(len(score_list)):
        if score_list[i] > max_score:
            max_score = score_list[i]
            max_index = i
    return max_index
