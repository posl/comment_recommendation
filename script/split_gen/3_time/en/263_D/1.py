def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] < l:
            ans += l
        elif a[i] > r:
            ans += r
        else:
            ans += a[i]
    print(ans)
