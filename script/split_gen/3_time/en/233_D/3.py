def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(n):
        a[i+1] += a[i]
    aa = sorted(a)
    ans = 0
    for i in range(n):
        l = i
        r = n - 1
        while r - l > 1:
            mid = (l + r) // 2
            if aa[mid] - aa[i] < k:
                l = mid
            else:
                r = mid
        if aa[r] - aa[i] == k:
            ans += 1
    print(ans)
