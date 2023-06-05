def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    d = {}
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if (A[i] + A[j]) % 200 not in d:
                d[(A[i] + A[j]) % 200] = (i, j)
            else:
                print('Yes')
                print(2, i, j)
                print(2, d[(A[i] + A[j]) % 200][0], d[(A[i] + A[j]) % 200][1])
                return
    print('No')
solve()
