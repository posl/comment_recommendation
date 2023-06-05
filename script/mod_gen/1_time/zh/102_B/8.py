def max_diff():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > max:
                max = abs(A[i] - A[j])
    print(max)
max_diff()
