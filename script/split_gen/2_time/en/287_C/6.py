def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print('No')
        return
    v = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        v[u - 1] += 1
        v[v - 1] += 1
    for i in v:
        if i != 1:
            print('No')
            return
    print('Yes')
    return
