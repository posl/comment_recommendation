def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i, N):
            if sum(A[i:j+1]) >= K:
                count += 1
    print(count)
