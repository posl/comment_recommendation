def get_min_max_oranges(A, B, W):
    min_oranges = 0
    max_oranges = 0
    for i in range(1, W*1000+1):
        if A <= (W*1000)/i <= B:
            if min_oranges == 0:
                min_oranges = i
            max_oranges = i
    return min_oranges, max_oranges
