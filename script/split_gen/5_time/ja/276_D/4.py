def func(n, a):
    cnt = 0
    while True:
        if len(set(a)) == 1 and 1 in set(a):
            return cnt
        if 1 in set(a):
            return -1
        a = [i//2 if i % 2 == 0 else i//3 for i in a]
        cnt += 1
