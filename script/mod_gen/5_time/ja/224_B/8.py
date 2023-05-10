def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    #print(a)
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if i == 0:
                a[i][j] += a[i][j-1]
            elif j == 0:
                a[i][j] += a[i-1][j]
            else:
                a[i][j] += max(a[i][j-1], a[i-1][j])
    #print(a)
    if a[h-1][w-1] == a[0][0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()