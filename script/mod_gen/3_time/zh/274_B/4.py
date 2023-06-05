def main():
    h,w = input().split()
    h = int(h)
    w = int(w)
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        print(count, end=' ')
    print()

if __name__ == '__main__':
    main()