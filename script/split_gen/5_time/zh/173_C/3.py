def main():
    h,w,k = map(int,input().split())
    c = [list(input()) for i in range(h)]
    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    if (i >> x) & 1 == 0 and (j >> y) & 1 == 0 and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
main()
