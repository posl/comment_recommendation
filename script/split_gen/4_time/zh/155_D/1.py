def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    a.reverse()
    a.append(0)
    a.reverse()
    l = 0
    r = n
    while r - l > 1:
        m = (l + r) // 2
        s = 0
        for i in range(n):
            if a[i] > 0:
                break
            if a[i] * a[i] <= a[m]:
                s += n - i - 1
            else:
                j = n - 1
                while a[i] * a[j] > a[m] and j > i:
                    j -= 1
                s += n - j - 1
        if s < k:
            l = m
        else:
            r = m
    print(a[r])
