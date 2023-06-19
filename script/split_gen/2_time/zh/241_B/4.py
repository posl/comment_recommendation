def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if N < M:
        print('No')
        return
    i = 0
    for a in A:
        if a == B[i]:
            i += 1
            if i == M:
                print('Yes')
                return
    print('No')
solve()
