def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                y1 = i
                x1 = j
            elif s[i][j] == 'x':
                y2 = i
                x2 = j
    ans = max(abs(x1-x2), abs(y1-y2))
    print(ans)

if __name__ == '__main__':
    main()