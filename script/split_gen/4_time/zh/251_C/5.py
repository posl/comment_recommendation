def judge_max_score(score_list):
    max_score = 0
    max_index = 0
    for index, score in enumerate(score_list):
        if score > max_score:
            max_score = score
            max_index = index
    return max_index
