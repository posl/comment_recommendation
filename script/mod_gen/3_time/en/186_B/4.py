def main():
    h,w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            count += a[i][j]
    print(count - h*w)

if __name__ == '__main__':
    main()