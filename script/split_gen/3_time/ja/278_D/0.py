def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9 + 7
    n = int(readline())
    a = list(map(int,readline().split()))
    q = int(readline())
    ans = sum(a)
    for _ in range(q):
        t,*query = map(int,readline().split())
        if t == 1:
            x = query[0]
            ans += n * x
        elif t == 2:
            i,x = query
            ans += x
        else:
            i = query[0]
            print(a[i - 1] + ans)
    return
