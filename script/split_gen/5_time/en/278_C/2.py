def main():
    n, q = map(int, input().split())
    follow = [[False] * n for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = True
        elif t == 2:
            follow[a][b] = False
        else:
            if follow[a][b]:
                print('Yes')
            else:
                print('No')
