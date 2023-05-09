def main():
    h,w = map(int,input().split())
    c = []
    for i in range(h):
        c.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()