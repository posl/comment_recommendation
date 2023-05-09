def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    time = 0
    for i in range(N):
        time += A[i] / B[i]
    time /= 2
    distance = 0
    for i in range(N):
        if time >= A[i] / B[i]:
            distance += A[i]
        else:
            distance += time * B[i]
    print(distance)
