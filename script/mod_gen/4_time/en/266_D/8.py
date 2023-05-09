def solve():
    N = int(input())
    Snukes = []
    for i in range(N):
        T, X, A = map(int, input().split())
        Snukes.append([T, X, A])
    Snukes.sort()
    Takahashi = 0
    for i in range(N):
        if Takahashi < Snukes[i][1]:
            Takahashi = Snukes[i][1]
        if Takahashi == Snukes[i][1]:
            Takahashi += 1
    return Takahashi - 1
print(solve())

if __name__ == '__main__':
    solve()