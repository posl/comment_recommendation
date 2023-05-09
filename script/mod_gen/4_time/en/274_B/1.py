def main():
    h, w = map(int, input().split())
    l = []
    for i in range(h):
        l.append(input())
    for j in range(w):
        count = 0
        for i in range(h):
            if l[i][j] == '#':
                count += 1
        print(count)

if __name__ == '__main__':
    main()