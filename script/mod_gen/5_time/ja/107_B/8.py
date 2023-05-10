def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    for i in range(h):
        if a[i].count("#") == w:
            continue
        else:
            for j in range(w):
                if a[i][j] == "#":
                    continue
                else:
                    if j == w-1:
                        a[i] = ""
                    else:
                        a[i] = a[i][:j] + a[i][j+1:]
                    w -= 1
                    break
    for k in range(w):
        if all(a[l][k] == "#" for l in range(h)):
            continue
        else:
            for m in range(h):
                if a[m][k] == "#":
                    continue
                else:
                    if m == h-1:
                        for n in range(h):
                            a[n] = a[n][:k] + a[n][k+1:]
                    else:
                        for n in range(h):
                            a[n] = a[n][:k] + a[n][k+1:]
                    h -= 1
                    break
    for o in range(h):
        print(a[o])

if __name__ == '__main__':
    main()