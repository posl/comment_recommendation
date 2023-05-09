def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i > 0 and j > 0:
                if a[i][j] + a[i - 1][j - 1] > a[i][j - 1] + a[i - 1][j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()