def main():
    import sys
    from bisect import bisect_left
    from collections import defaultdict
    input = sys.stdin.readline
    N, C = map(int, input().split())
    service = [list(map(int, input().split())) for _ in range(N)]
    service.sort()
    #print(service)
    #print(N, C)
    #print(service)
    #print(service)
    s = defaultdict(int)
    for i in range(N):
        s[service[i][0]] += service[i][2]
        s[service[i][1] + 1] -= service[i][2]
    #print(s)
    d = [0]
    for i in range(1, 10 ** 9 + 1):
        d.append(d[-1] + s[i])
    #print(d)
    ans = 10 ** 20
    for i in range(1, 10 ** 9 + 1):
        ans = min(ans, d[bisect_left(d, C)])
    print(ans)
