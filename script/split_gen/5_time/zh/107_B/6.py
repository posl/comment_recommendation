def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for j in range(W):
        if '#' in [a[i][j] for i in range(H)]:
            c.append([a[i][j] for i in range(H)])
    for i in range(len(b)):
        print(''.join([c[j][i] for j in range(len(c))]))
