def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    h = [False for _ in range(H)]
    w = [False for _ in range(W)]
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                h[i] = True
                w[j] = True
    for i in range(H):
        if h[i]:
            for j in range(W):
                if w[j]:
                    print(a[i][j], end='')
            print()
    return
