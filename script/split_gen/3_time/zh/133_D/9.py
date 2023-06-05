def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i % 2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]
    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]
    print(' '.join(map(str, ans)))
