def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(w):
        s = 0
        for j in range(h):
            if a[j][i] == "#":
                s += 1
        print(s)

if __name__ == '__main__':
    main()