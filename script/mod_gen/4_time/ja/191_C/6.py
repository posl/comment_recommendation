def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                ans += 1
    if ans == h+w-1:
        print(1)
    elif ans == h+w-2:
        print(2)
    else:
        print(4)

if __name__ == '__main__':
    main()