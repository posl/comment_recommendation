def get_subordinates_num(n, superiors):
    subordinates = [0] * n
    for i in superiors:
        subordinates[i - 1] += 1
    return subordinates
