def find_min_max_oranges(A,B,W):
    min_oranges = 0
    max_oranges = 0
    min_weight = A * 1000
    max_weight = B * 1000
    total_weight = W * 1000
    if min_weight > total_weight:
        return "UNSATISFIABLE"
    else:
        min_oranges = total_weight // max_weight
        max_oranges = total_weight // min_weight
        if total_weight % max_weight != 0:
            min_oranges += 1
        if total_weight % min_weight != 0:
            max_oranges += 1
        return str(min_oranges) + " " + str(max_oranges)

if __name__ == '__main__':
    find_min_max_oranges()