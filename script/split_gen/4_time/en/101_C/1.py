def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-K):
        if A[i] < A[i+K]:
            cnt += 1
    print(cnt+1)
