def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(w):
        for j in range(h):
            print(a[j][i], end="")
            if j != h-1:
                print(" ", end="")
        print()

if __name__ == '__main__':
    main()