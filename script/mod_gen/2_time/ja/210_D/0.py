def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j), a[i][j] + c * ((h-1-i) + (w-1-j)))
    print(ans)

if __name__ == '__main__':
    main()