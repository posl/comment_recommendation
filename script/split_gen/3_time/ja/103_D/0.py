def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        ans = max(ans, b[i] - a[i] - 1)
    print(ans)
