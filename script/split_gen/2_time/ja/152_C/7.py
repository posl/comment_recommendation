def main():
    #入力
    N = int(input())
    P = list(map(int,input().split()))
    #処理
    ans = 0
    mi = P[0]
    for i in range(1,N):
        if mi >= P[i]:
            ans += 1
        mi = min(mi,P[i])
    ans += 1
    #出力
    print(ans)
main()
