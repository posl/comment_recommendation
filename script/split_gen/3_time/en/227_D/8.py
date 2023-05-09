def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        if i < k:
            ans += a[i]
        else:
            ans += a[i] - 1
    print(ans)
