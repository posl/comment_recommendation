def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if M * N - sum > K:
        print(-1)
    elif M * N - sum <= 0:
        print(0)
    else:
        print(M * N - sum)
