def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aをソート
    A.sort()
    #bの候補を作成
    b = [A[N//2-1], A[N//2]]
    #悲しさの値の最小値を求める
    ans = float('inf')
    for i in range(len(b)):
        tmp = 0
        for j in range(N):
            tmp += abs(A[j] - (b[i] + j - N//2))
        ans = min(ans, tmp)
    #出力
    print(ans)

if __name__ == '__main__':
    main()