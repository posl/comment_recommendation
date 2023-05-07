def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    n, x = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    d = defaultdict(int)
    for i in range(n):
        for j in range(1, l[i][0]+1):
            d[l[i][j]] += 1
    ans = 0
    for i in d:
        if i != 1 and x % i == 0 and d[x//i] > 0:
            if i == x // i:
                ans += d[i] * (d[i]-1) // 2
            else:
                ans += d[i] * d[x//i]
    print(ans)
