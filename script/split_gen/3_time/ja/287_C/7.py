def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print('No')
        return
    d = [0 for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        d[u - 1] += 1
        d[v - 1] += 1
    for i in range(n):
        if d[i] != 1:
            print('No')
            return
    print('Yes')
