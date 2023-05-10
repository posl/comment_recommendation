def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
            ans += 2 * A[i] * L
        else:
            ans += 2 * A[i] * R
    ans -= (L + R) * (max(A) - min(A))
    print(ans)
main()
