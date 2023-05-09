def main():
    h, w = map(int, input().split())
    g = [list(input()) for i in range(h)]
    i = 0
    j = 0
    while True:
        if g[i][j] == "U":
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif g[i][j] == "D":
            if i == h-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif g[i][j] == "L":
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif g[i][j] == "R":
            if j == w-1:
                print(i+1, j+1)
                break
            else:
                j += 1
        else:
            print(i+1, j+1)
            break
    return 0

if __name__ == '__main__':
    main()