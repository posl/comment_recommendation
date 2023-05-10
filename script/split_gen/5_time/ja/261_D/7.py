def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    YC = [list(map(int, input().split())) for _ in range(M)]
    YC.sort(key=lambda x: x[1], reverse=True)
    YC.sort(key=lambda x: x[0])
    YC = [[0, 0]] + YC
    YC.append([N+1, 0])
    #print(YC)
    ans = 0
    for i in range(1, M+2):
        if i == 1:
            ans += sum(X)
        else:
            ans += sum(X[YC[i-2][0]-1:YC[i-1][0]-1])
        #print(ans)
        ans += (YC[i][0]-YC[i-1][0])*YC[i-1][1]
        #print(ans)
    print(ans)
    return
main()
