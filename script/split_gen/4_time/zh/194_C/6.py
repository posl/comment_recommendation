def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (N - i) * (A[i] ** 2)
        ans -= 2 * A[i] * sum(A[:i])
        ans += sum(A[:i]) ** 2
    print(ans)
