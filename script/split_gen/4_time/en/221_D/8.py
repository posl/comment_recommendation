def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_day = max(A) + max(B)
    day = [0] * (max_day + 1)
    for i in range(N):
        day[A[i] - 1] += 1
        day[A[i] + B[i] - 1] -= 1
    for i in range(max_day):
        day[i + 1] += day[i]
    for i in range(max_day):
        if day[i] > N:
            day[i] = N
    print(*day[:max_day], sep=" ")
