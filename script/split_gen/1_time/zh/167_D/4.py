def problem167_d():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * n
    B[0] = 1
    for i in range(n):
        if B[A[i]-1] == 0:
            B[A[i]-1] = 1
        else:
            break
    k = k % i
    for j in range(k):
        A = [A[a]-1 for a in range(n)]
    print(A[0]+1)
