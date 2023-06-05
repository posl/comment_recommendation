def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(list(input()))
    h = [0] * H
    w = [0] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                h[i] = 1
                w[j] = 1
    for i in range(H):
        if h[i] == 1:
            for j in range(W):
                if w[j] == 1:
                    print(a[i][j], end = '')
            print()
main()
