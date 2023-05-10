def count_ways(L):
    # base cases
    if L < 12:
        return 0
    if L == 12:
        return 1
    # recursive case
    return count_ways(L-1) + count_ways(L-4) + count_ways(L-7) + count_ways(L-10) + count_ways(L-13) + count_ways(L-16)
