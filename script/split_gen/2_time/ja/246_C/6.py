def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                ans += A[i] - X
                K -= 1
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)
