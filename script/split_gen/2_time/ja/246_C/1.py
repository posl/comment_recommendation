def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i] - X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)
