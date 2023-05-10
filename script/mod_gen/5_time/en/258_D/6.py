def solve():
    N,X = map(int,input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort()
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X:
            print(ans)
            return
    print(ans)
    return

if __name__ == '__main__':
    solve()