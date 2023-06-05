def solve(N, A):
    cnt = 0
    while True:
        flg = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            elif A[i] % 3 == 0:
                A[i] //= 3
            else:
                flg = False
                break
        if flg:
            cnt += 1
        else:
            break
    if all([a == A[0] for a in A]):
        return cnt
    else:
        return -1
N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))
