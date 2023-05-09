def solve():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 10**6)
    for i in range(1, N-2):
        print(i, i+3, 1)
    for i in range(1, N-2):
        print(i, i+3, 10**6-1)
    for i in range(1, N-2):
        print(i, i+3, 2*(10**6-1))
    L -= 3*(N-3)
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 10**6-2)
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 2*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 3*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 4*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 5*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 6*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 7*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+

if __name__ == '__main__':
    solve()