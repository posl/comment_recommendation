def main():
    h, w = map(int, input().split())
    #print(h, w)
    c = []
    for i in range(h):
        c.append(input())
    #print(c)
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == "#":
                x += 1
        print(x, end = " ")
    print()

if __name__ == '__main__':
    main()