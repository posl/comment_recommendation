def calc_penalty(problems, penalty):
    penalty_total = 0
    for i in range(len(problems)):
        if problems[i] == "AC":
            penalty_total += penalty[i]
    return penalty_total
