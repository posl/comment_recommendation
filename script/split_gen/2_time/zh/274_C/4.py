def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = i + 1
    for i in range(1, N + 1):
        j = i
        while j != 1:
            ans[j // 2] = max(ans[j // 2], ans[j] + 1)
            j //= 2
    for i in range(1, 2 * N + 1):
        print(ans[i])
