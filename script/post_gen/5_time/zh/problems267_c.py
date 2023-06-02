Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_max_sum(n, m, a):
    #print("n: %d, m: %d" % (n, m))
    #print(a)
    max_sum = 0
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += (j+1)*a[i+j]
        if sum > max_sum:
            max_sum = sum
    return max_sum

=======
Suggestion 3

def sum_of_subarrays(a):
    n = len(a)
    result = 0
    for i in range(n):
        for j in range(i, n):
            result += (j-i+1) * sum(a[i:j+1])
    return result

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if a[i] == 0:
            continue
        else:
            b.append(a[i])
    if len(b) < m:
        print(0)
    else:
        b.sort(reverse = True)
        ans = 0
        for i in range(m):
            ans += (i+1)*b[i]
        print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    for i in range(1, m + 1):
        ans = max(ans, s[i] - min(s[:i]))
    for i in range(m + 1, n + 1):
        ans = max(ans, s[i] - min(s[i - m:i]))
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    from collections import deque
    q = deque()
    q.append((0, 0))
    res = -float('inf')
    for i in range(1, n + 1):
        while q and q[0][0] < i - m:
            q.popleft()
        res = max(res, s[i] - q[0][1])
        while q and q[-1][1] >= s[i]:
            q.pop()
        q.append((i, s[i]))
    print(res)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + a[i]
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        c[i] = max(c[i - 1], b[i])
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = max(d[i - 1], c[i] + b[i])
    e = [0] * (n + 1)
    for i in range(1, n + 1):
        e[i] = max(e[i - 1], d[i] + b[i])
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = max(f[i - 1], e[i] + b[i])
    g = [0] * (n + 1)
    for i in range(1, n + 1):
        g[i] = max(g[i - 1], f[i] + b[i])
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = max(h[i - 1], g[i] + b[i])
    i = [0] * (n + 1)
    for i in range(1, n + 1):
        i[i] = max(i[i - 1], h[i] + b[i])
    j = [0] * (n + 1)
    for i in range(1, n + 1):
        j[i] = max(j[i - 1], i[i] + b[i])
    k = [0] * (n + 1)
    for i in range(1, n + 1):
        k[i] = max(k[i - 1], j[i] + b[i])
    l = [0] * (n + 1)
    for i in range(1, n +

=======
Suggestion 8

def max_sum(n, m, a):
    if m == 1:
        return max(a)
    if m == 2:
        return max(a[0] + a[1], a[-1] + a[-2])
    if m == 3:
        return max(a[0] + a[1] + a[2], a[-1] + a[-2] + a[-3], a[0] + a[1] + a[-1], a[0] + a[-2] + a[-1], a[-1] + a[-2] + a[0])
    if m == 4:
        return max(a[0] + a[1] + a[2] + a[3], a[-1] + a[-2] + a[-3] + a[-4], a[0] + a[1] + a[-1] + a[-2], a[0] + a[-1] + a[-2] + a[-3], a[-1] + a[-2] + a[-3] + a[0], a[0] + a[1] + a[2] + a[-1], a[0] + a[1] + a[-2] + a[-1], a[0] + a[-1] + a[-2] + a[-3], a[-1] + a[-2] + a[-3] + a[0])
    if m == 5:
        return max(a[0] + a[1] + a[2] + a[3] + a[4], a[-1] + a[-2] + a[-3] + a[-4] + a[-5], a[0] + a[1] + a[-1] + a[-2] + a[-3], a[0] + a[-1] + a[-2] + a[-3] + a[-4], a[-1] + a[-2] + a[-3] + a[-4] + a[0], a[0] + a[1] + a[2] + a[3] + a[-1], a[0] + a[1] + a[2] + a[-2] + a[-1], a[0] + a[1] + a[-1

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(n + 1):
        if i % m == 0:
            l[i] = s[i]
        else:
            l[i] = max(l[i - 1], s[i])
    for i in range(n, -1, -1):
        if i % m == 0:
            r[i] = s[i]
        else:
            r[i] = max(r[i + 1], s[i])
    ans = 0
    for i in range(1, n):
        ans = max(ans, l[i] + r[i + 1] - s[i])
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        ans += (i + 1) * a[i]
    tmp = ans
    for i in range(m, n):
        tmp += (i + 1) * a[i] - i * a[i - m]
        ans = max(tmp, ans)
    print(ans)

main()
