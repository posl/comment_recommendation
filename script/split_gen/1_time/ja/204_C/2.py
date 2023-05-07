def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N*N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    AB = [[0,0]] + AB + [[N+1,N+1]]
    ans = 0
    for i in range(1,M+1):
        if AB[i][0] == AB[i-1][0]:
            if AB[i][1] != AB[i-1][1] + 1:
                ans += (AB[i][1] - AB[i-1][1] - 1) * (AB[i][1] - AB[i-1][1] - 2) // 2
        else:
            ans += (AB[i][1] - 1) * (AB[i][1] - 2) // 2
            ans += (N - AB[i-1][1]) * (N - AB[i-1][1] - 1) // 2
    print(ans)
