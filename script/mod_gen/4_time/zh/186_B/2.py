def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_v = 101
    for i in range(h):
        for j in range(w):
            min_v = min(a[i][j],min_v)
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_v
    print(ans)

if __name__ == '__main__':
    main()