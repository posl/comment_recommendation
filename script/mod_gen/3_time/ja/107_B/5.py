def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    Hlist = []
    Wlist = []
    for i in range(H):
        if '#' not in a[i]:
            Hlist.append(i)
    for j in range(W):
        if '#' not in [a[i][j] for i in range(H)]:
            Wlist.append(j)
    for i in range(H):
        if i not in Hlist:
            print(''.join([a[i][j] for j in range(W) if j not in Wlist]))
    return

if __name__ == '__main__':
    main()