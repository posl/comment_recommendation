def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i]*A[k] == A[j]**2:
                    cnt += 1
                if A[j]*A[k] == A[i]**2:
                    cnt += 1
    print(cnt)
    return 0
