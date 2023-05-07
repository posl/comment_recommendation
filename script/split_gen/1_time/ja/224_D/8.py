def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    d = defaultdict(list)
    for i in range(n):
        u,v = map(int,input().split())
        d[u].append(v)
        d[v].append(u)
    s = list(map(int,input().split()))
    for i in range(9):
        if len(d[i+1]) == 0:
            d[i+1] = [-1]
    ans = 0
    for i in range(8):
        if s[i] == i+1:
            continue
        if s[i] in d[s[i+1]]:
            ans += 1
            s[i],s[i+1] = s[i+1],s[i]
        else:
            ans = -1
            break
    print(ans)
