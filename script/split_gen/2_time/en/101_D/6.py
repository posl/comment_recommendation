def snuke_numbers(k):
    s = 0
    for i in range(1, k + 1):
        s += i
        if s > 9:
            s = s % 9
        if s == 1 or s == 3 or s == 6 or s == 8:
            print(i)
