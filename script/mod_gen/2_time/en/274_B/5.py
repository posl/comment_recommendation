def main():
    h, w = map(int, input().split())
    l = []
    for i in range(h):
        l.append(input())
    c = []
    for i in range(w):
        c.append(0)
    for i in range(w):
        for j in range(h):
            if l[j][i] == "#":
                c[i] += 1
    print(*c)

if __name__ == '__main__':
    main()