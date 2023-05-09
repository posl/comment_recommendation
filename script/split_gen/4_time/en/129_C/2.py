def main():
    n, m = map(int, input().split())
    a = [0] * (m + 2)
    a[0] = 0
    a[m + 1] = n + 1
    for i in range(1, m + 1):
        a[i] = int(input())
    a.sort()
    d = [0] * (m + 2)
    d[0] = 1
    d[1] = 1
    for i in range(2, m + 2):
        d[i] = d[i - 1] + d[i - 2]
    ans = 1
    for i in range(1, m + 2):
        ans *= d[a[i] - a[i - 1] - 1]
        ans %= 1000000007
    print(ans)
