def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if not all(a[i][j] == "." for j in range(w)):
            b.append(a[i])
    c = []
    for j in range(w):
        if not all(a[i][j] == "." for i in range(h)):
            c.append(j)
    for i in range(len(b)):
        for j in c:
            print(b[i][j],end="")
        print()

if __name__ == '__main__':
    main()