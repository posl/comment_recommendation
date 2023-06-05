def solve(N, A):
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                return cnt
        cnt += 1
