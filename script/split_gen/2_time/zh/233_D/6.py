def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N+1)
    for i in range(N):
        sum_A[i+1] = sum_A[i] + A[i]
    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum_A[j] - sum_A[i] == K:
                count += 1
    print(count)
