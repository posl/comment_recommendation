def sum_of_subset(w, subset):
    sum = 0
    for i in subset:
        sum += w[i]
    return sum
