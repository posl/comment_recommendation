def solve():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.insert(0, 0)
    for i in range(1, N+1):
        for j in range(i+1, N+2):
            if A[i] + A[j] <= abs(x-y):
                print('Yes')
                return
    print('No')
