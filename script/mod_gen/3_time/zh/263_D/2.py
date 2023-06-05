def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if l == r == 0:
        print(sum(a))
        return
    if l > r:
        l, r = r, l
    if a[0] >= 0:
        print(sum(a) + l * (n - 1))
        return
    if a[-1] <= 0:
        print(sum(a) + r * (n - 1))
        return
    i = 0
    while i < n and a[i] > 0:
        i += 1
    if i == n:
        print(sum(a) + l * (n - 1))
        return
    j = i
    while j < n and a[j] == 0:
        j += 1
    if j == n:
        print(sum(a) + l * (n - 1))
        return
    k = j
    while k < n and a[k] < 0:
        k += 1
    if k == n:
        print(sum(a) + r * (n - 1))
        return
    ans = 0
    for x in range(i):
        ans += a[x] * (l + r)
    for x in range(i, j):
        ans += a[x] * (l + r)
    for x in range(j, k):
        ans += a[x] * (l + r)
    for x in range(k, n):
        ans += a[x] * (l + r)
    print(ans)

if __name__ == '__main__':
    main()