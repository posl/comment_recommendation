def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(Y+1)] for j in range(X+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(X,-1,-1):
            for k in range(Y,-1,-1):
                if dp[j][k] == 1:
                    dp[min(j+A[i],X)][min(k+B[i],Y)] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if dp[X-i][Y-j] == 1:
                print(N-i)
                exit()
    print(-1)
