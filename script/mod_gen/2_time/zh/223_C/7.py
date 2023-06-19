def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        ans += AB[i][0] / AB[i][1]
    ans /= 2
    print(ans)

if __name__ == '__main__':
    solve()