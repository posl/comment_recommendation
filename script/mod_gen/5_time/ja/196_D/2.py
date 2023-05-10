def solve():
    h,w,a,b = map(int,input().split())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k in range(h):
                if i>>k&1:
                    cnt += w
                else:
                    if j>>k&1:
                        cnt += 1
            if cnt == a:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()