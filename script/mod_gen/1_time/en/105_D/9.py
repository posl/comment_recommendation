def main():
    from sys import stdin
    from collections import defaultdict
    n,m = map(int,stdin.readline().strip().split())
    a = list(map(int,stdin.readline().strip().split()))
    s = [0]
    for i in range(n):
        s.append((s[i]+a[i])%m)
    d = defaultdict(int)
    for i in range(n+1):
        d[s[i]] += 1
    ans = 0
    for k,v in d.items():
        ans += v*(v-1)//2
    print(ans)
main()
