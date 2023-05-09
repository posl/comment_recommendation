def main():
    #入力
    N = int(input())
    V = list(map(int,input().split()))
    C = list(map(int,input().split()))
    #処理
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    #出力
    print(ans)

if __name__ == '__main__':
    main()