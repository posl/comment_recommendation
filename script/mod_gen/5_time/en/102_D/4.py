def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    r = float('inf')
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            p = s[i]
            q = s[j] - s[i]
            r = s[n] - s[j]
            s1 = max(p, q, r)
            s2 = min(p, q, r)
            r = min(r, s1 - s2)
    print(r)

if __name__ == '__main__':
    solve()