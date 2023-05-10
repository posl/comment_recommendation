def calc_penalty(penalty_list):
    penalty = 0
    for i in range(len(penalty_list)):
        penalty += penalty_list[i]
    return penalty
