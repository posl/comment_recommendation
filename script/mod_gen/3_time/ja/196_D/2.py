def solve():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            count = 0
            for k in range(H):
                for l in range(W):
                    if (i>>k)&1 == 0 and (j>>l)&1 == 0:
                        count += 1
            if count == A:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()