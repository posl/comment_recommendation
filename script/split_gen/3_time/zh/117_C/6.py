def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(x[-1] - x[0])
        return
    x_diff = []
    for i in range(1, m):
        x_diff.append(x[i] - x[i - 1])
    x_diff.sort()
    ans = 0
    for i in range(m - n):
        ans += x_diff[i]
    print(ans)
