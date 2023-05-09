def main():
    N = int(input())
    A = [0]*N
    x = [[0]*N for i in range(N)]
    y = [[0]*N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(1<<N):
        flag = True
        for j in range(N):
            if (i>>j)&1:
                for k in range(A[j]):
                    if (i>>(x[j][k]-1))&1 != y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
