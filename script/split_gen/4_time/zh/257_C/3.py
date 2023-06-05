def f(x):
    count = 0
    for i in range(n):
        if s[i] == "0":
            if w[i] < x:
                count += 1
        else:
            if w[i] >= x:
                count += 1
    return count
