def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    h = []
    for i in range(H):
        if a[i].count(".") != W:
            h.append(a[i])
    w = []
    for i in range(W):
        cnt = 0
        for j in range(H):
            if a[j][i] == ".":
                cnt += 1
        if cnt != H:
            w.append(i)
    for i in range(len(h)):
        for j in range(len(w)):
            print(h[i][w[j]], end="")
        print()

if __name__ == '__main__':
    main()