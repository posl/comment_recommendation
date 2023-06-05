def solve():
    N = int(input())
    A = list(map(int, input().split()))
    x = 0
    max_x = 0
    for i in range(N):
        x += A[i]
        max_x = max(max_x, x)
    print(max_x)
