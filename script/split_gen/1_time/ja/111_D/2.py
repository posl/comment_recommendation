def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = []
    for i in range(N):
        if (X[i] + Y[i]) % 2 == 0:
            ans.append('U')
        else:
            ans.append('R')
    if ans.count('U') == N or ans.count('R') == N:
        print(N)
        print(*ans, sep='
')
    else:
        print(-1)
