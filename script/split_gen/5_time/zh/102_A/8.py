def get_min_number(n):
    min_number = 0
    while True:
        min_number += n
        if min_number % 2 == 0 and min_number % n == 0:
            break
    return min_number
