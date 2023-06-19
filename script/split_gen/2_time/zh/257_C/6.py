def solve(n, s, w):
    s = list(s)
    w = list(w)
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        cnt = 0
        for i in range(n):
            if s[i] == '0':
                if w[i] <= mid:
                    cnt += 1
            else:
                if w[i] > mid:
                    cnt += 1
        if cnt == n:
            l = mid
        else:
            r = mid
    return l
n = int(input())
s = input()
w = input().split()
print(solve(n, s, w))
