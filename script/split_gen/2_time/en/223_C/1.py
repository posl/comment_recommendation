def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    ans = 0
    for i in range(n):
        ans += a[i]/b[i]
    ans /= 2
    print(ans)
