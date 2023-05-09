def main():
    import sys
    from collections import defaultdict
    n,m = map(int, sys.stdin.readline().split())
    if m == 0:
        print(n**2)
        return
    dic = defaultdict(set)
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        dic[a].add(b)
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if j in dic[i]:
                continue
            ans += 1
    print(ans)
