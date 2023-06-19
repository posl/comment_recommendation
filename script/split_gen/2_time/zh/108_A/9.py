def count_even_odd_pairs(k):
    # k is an integer
    # return the number of ways to choose a pair of
    # even number and odd number from 1, 2, ..., k
    count = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            if i % 2 == 0 and j % 2 != 0:
                count += 1
    return count
