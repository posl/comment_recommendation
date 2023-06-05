def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = sum(A)
    half = total / 2
    time = 0
    for i in range(N):
        time += A[i] / B[i]
        if time >= half:
            print(half * 2 - total)
            break
