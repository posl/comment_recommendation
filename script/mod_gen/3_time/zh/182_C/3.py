def solve(N):
    if N % 3 == 0:
        return 0
    elif N % 3 == 1:
        if N % 10 == 1:
            return -1
        elif N % 10 == 4:
            return -1
        elif N % 10 == 7:
            return -1
        else:
            return 1
    else:
        if N % 10 == 2:
            return -1
        elif N % 10 == 5:
            return -1
        elif N % 10 == 8:
            return -1
        else:
            return 1

if __name__ == '__main__':
    solve()