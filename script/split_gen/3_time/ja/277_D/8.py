def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i%m for i in a]
    a.sort()
    a.append(a[0]+m)
    ans = 0
    for i in range(n):
        if a[i] > a[i+1]:
            ans += m - a[i] + a[i+1]
        else:
            ans += a[i+1] - a[i]
    print(ans)
