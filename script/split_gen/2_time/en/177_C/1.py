def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += A[i] * S
        ans %= 10 ** 9 + 7
    print(ans)
