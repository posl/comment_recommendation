def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i, N):
            sum += A[j]
            if sum == K:
                print(i, j)
    print(sum)
