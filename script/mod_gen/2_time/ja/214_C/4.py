def main():
    #入力
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    #処理
    ans = [0]*N
    for i in range(N):
        ans[i] = T[i]
        for j in range(N):
            if T[i] < ans[(i+j)%N]:
                ans[(i+j)%N] = T[i] + sum(S[(i+j)%N:(i+j)%N+j+1])
    #出力
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()