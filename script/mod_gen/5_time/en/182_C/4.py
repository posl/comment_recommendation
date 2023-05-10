def solve():
    N = input()
    k = len(N)
    N = list(N)
    N.sort(reverse=True)
    N = ''.join(N)
    N = int(N)
    if N % 3 == 0:
        return 0
    elif N % 3 == 1:
        if k == 1:
            return -1
        elif k == 2:
            return -1
        elif k == 3:
            if N % 3 == 1:
                return 1
            elif N % 3 == 2:
                return 2
        else:
            for i in range(k):
                if int(N[i]) % 3 == 1:
                    return 1
                elif int(N[i]) % 3 == 2:
                    return 2
            return -1
    elif N % 3 == 2:
        if k == 1:
            return -1
        elif k == 2:
            return -1
        elif k == 3:
            if N % 3 == 1:
                return 2
            elif N % 3 == 2:
                return 1
        else:
            for i in range(k):
                if int(N[i]) % 3 == 1:
                    return 2
                elif int(N[i]) % 3 == 2:
                    return 1
            return -1
print(solve())

if __name__ == '__main__':
    solve()