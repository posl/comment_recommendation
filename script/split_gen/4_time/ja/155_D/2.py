def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = 0
    r = 0
    for i in range(n):
        if a[i] < 0:
            l += 1
        else:
            r += 1
    ans = 0
    if l * r >= k:
        for i in range(l):
            for j in range(r):
                ans += 1
                if ans == k:
                    print(a[i] * a[n - 1 - j])
                    exit()
    else:
        for i in range(l):
            for j in range(i + 1, l):
                ans += 1
                if ans == k:
                    print(a[i] * a[j])
                    exit()
        for i in range(r):
            for j in range(i + 1, r):
                ans += 1
                if ans == k:
                    print(a[n - 1 - i] * a[n - 1 - j])
                    exit()
        for i in range(l):
            for j in range(r):
                ans += 1
                if ans == k:
                    print(a[i] * a[n - 1 - j])
                    exit()
