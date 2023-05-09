def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(1, N):
        ans[i] = 2 * a[i - 1] - ans[i - 1]
    print(*ans)
