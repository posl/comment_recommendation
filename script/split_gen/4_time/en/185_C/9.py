def divide(l):
    # base case
    if l == 1:
        return 1
    # recursive case
    else:
        return sum([divide(l-i) for i in range(1, l)])
