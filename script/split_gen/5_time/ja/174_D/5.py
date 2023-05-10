def solve():
    N = int(input())
    C = input()
    r = 0
    w = 0
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
        return
    if C[0] == 'R':
        r -= 1
    else:
        w -= 1
    if C[N-1] == 'W':
        w -= 1
    else:
        r -= 1
    print(min(r,w))
    return
