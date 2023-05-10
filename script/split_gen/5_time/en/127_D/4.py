def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        while b > 0 and i < N and c > A[i]:
            A[i] = c
            i += 1
            b -= 1
        if b == 0:
            break
    print(sum(A))
