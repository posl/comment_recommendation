def compute_rainfall(N, A):
    rain = [0] * N
    for i in range(N):
        if i == 0:
            rain[0] = A[0] - A[N-1] / 2 - A[1] / 2
        elif i == N-1:
            rain[N-1] = A[N-1] - A[N-2] / 2 - A[0] / 2
        else:
            rain[i] = A[i] - A[i-1] / 2 - A[i+1] / 2
    return rain
N = int(input())
A = list(map(int, input().split()))
print(*compute_rainfall(N, A))
