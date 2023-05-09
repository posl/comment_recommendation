def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += M // A[i]
        ans -= (M // (A[i] * 2)) - (M // (A[i] * 3))
    print(ans)
