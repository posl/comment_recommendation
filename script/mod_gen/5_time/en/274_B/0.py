def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if c[j][i] == '#':
                count += 1
        print(count)

if __name__ == '__main__':
    main()