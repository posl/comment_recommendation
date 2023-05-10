def S(n):
    n_str = str(n)
    sum = 0
    for i in range(len(n_str)):
        sum += int(n_str[i])
    return sum
