def main():
    h,w,x,y = map(int,input().split())
    s = []
    for i in range(h):
        s.append(list(input()))
    ans = 1
    for i in range(x-1,-1,-1):
        if s[i][y-1] == ".":
            ans += 1
        else:
            break
    for i in range(x,h):
        if s[i][y-1] == ".":
            ans += 1
        else:
            break
    for i in range(y-1,-1,-1):
        if s[x-1][i] == ".":
            ans += 1
        else:
            break
    for i in range(y,w):
        if s[x-1][i] == ".":
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()