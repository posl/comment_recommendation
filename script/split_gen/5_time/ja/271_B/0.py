def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    n,q = map(int,readline().split())
    a = []
    for _ in range(n):
        a.append(list(map(int,readline().split())))
    for _ in range(q):
        s,t = map(int,readline().split())
        print(a[s-1][t-1])
