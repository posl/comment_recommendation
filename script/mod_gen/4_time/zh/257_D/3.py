def solve():
    N = int(input())
    xyp = []
    for i in range(N):
        xyp.append(list(map(int, input().split())))
    #print(xyp)
    xyp.sort(key=lambda x: x[2])
    #print(xyp)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if xyp[i][2] * ans >= abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1]):
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    solve()