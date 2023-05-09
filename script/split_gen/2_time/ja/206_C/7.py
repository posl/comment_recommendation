def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += N - (i + 1) - (A[i] - A[i - 1]) * (N - (i + 1))
    print(ans)
