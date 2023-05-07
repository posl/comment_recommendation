def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        if i < N//2:
            ans += min(L, A[i])
        else:
            ans += min(R, A[i])
    print(ans)
