def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] >= K:
            ans = N - i
            break
    print(ans)
