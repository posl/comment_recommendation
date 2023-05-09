def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #ソート
    A.sort()
    B.sort()
    #初期化
    i = 0
    j = 0
    ans = 10**9
    #A,Bの要素を比較
    while i < N and j < M:
        ans = min(ans, abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()