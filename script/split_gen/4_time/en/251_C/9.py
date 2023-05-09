def main():
    import sys
    import collections
    n = int(input())
    l = []
    for i in range(n):
        s, t = input().split()
        l.append([s, int(t)])
    d = collections.defaultdict(int)
    for i in range(n):
        s, t = l[i]
        d[s] += t
    m = max(d.values())
    for i in range(n):
        s, t = l[i]
        if d[s] == m:
            print(i+1)
            sys.exit()
    print('error')
