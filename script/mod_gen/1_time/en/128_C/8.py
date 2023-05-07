def solve():
    N, M = map(int, input().split())
    bulbs = [list(map(int, input().split())) for i in range(M)]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for k in range(1, bulbs[j][0]+1):
                if i >> (bulbs[j][k]-1) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()