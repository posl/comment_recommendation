def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum >= K:
                count += N - j
                break
    print(count)
