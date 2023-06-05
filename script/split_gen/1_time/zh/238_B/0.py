def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a[i] = a[i] % 360
    a.sort()
    for i in range(n):
        a.append(a[i] + 360)
    for i in range(n):
        ans = max(ans, a[i+n-1] - a[i])
    print(360 - ans)
