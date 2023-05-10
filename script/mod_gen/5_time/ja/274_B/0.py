def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in range(w):
        x = 0
        for j in range(h):
            if a[j][i] == "#":
                x += 1
        print(x, end=" ")

if __name__ == '__main__':
    main()