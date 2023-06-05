def main():
    h,w,x,y = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    ans = 1
    for i in range(x-2, -1, -1):
        if a[i][y-1] == '#':
            break
        else:
            ans += 1
    for i in range(x, h):
        if a[i][y-1] == '#':
            break
        else:
            ans += 1
    for i in range(y-2, -1, -1):
        if a[x-1][i] == '#':
            break
        else:
            ans += 1
    for i in range(y, w):
        if a[x-1][i] == '#':
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()