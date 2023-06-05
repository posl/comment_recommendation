def solve(k):
    if k % 2 == 0 or k % 5 == 0:
        return -1
    else:
        x = 7
        for i in range(1, k + 1):
            if x % k == 0:
                return i
            else:
                x = x * 10 + 7
