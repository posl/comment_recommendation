def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i + 1)
        ans -= A[i] * (N - i - 1)
    print(ans)
