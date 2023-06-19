def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        X.append(int(input().split()[0]))
        Y.append(int(input().split()[1]))
    X.sort()
    Y.sort()
    x = X[N//2]
    y = Y[N//2]
    ans = 0
    for i in range(N):
        ans += abs(x-X[i])+abs(y-Y[i])
    print(ans)
main()
