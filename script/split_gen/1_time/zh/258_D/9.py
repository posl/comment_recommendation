def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    ans = 0
    for i in range(N):
        if B[i] > A[i]:
            ans += A[i] * X
        else:
            ans += B[i] * X
    print(ans)
