def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #ソート
    A.sort()
    #初期化
    ans = 0
    #ループ
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += (i+1)
    #出力
    print(ans)
