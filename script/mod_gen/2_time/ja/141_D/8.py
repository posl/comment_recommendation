def main():
    #入力
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #ソート
    A.sort(reverse=True)
    #割引券の枚数をカウント
    count = [0]*M
    for i in range(M):
        count[i] = count[i-1]+2**i
    #割引券の枚数をカウント
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i]//count[j] >= 1:
                ans += A[i]//count[j]
                A[i] = A[i]%count[j]
                break
    print(ans)

if __name__ == '__main__':
    main()