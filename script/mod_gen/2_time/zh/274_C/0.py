def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(input()))
    for i in range(w):
        c = 0
        for j in range(h):
            if a[j][i] == '#':
                c += 1
        print(c)

if __name__ == '__main__':
    main()