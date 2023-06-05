def solve():
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i == i2 and j == j2:
                        continue
                    ans = min(ans, a[i][j] + a[i2][j2] + c*(abs(i-i2)+abs(j-j2)))
    print(ans)

if __name__ == '__main__':
    solve()