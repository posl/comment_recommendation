def count753(N):
    if N < 3:
        return 0
    if N == 3:
        return 1
    if N > 3:
        n = 0
        for i in range(3, N + 1):
            if '3' in str(i) and '5' in str(i) and '7' in str(i):
                n += 1
        return n
