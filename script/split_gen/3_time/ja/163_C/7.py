def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #社員数分のリストを作成
    ans = [0] * N
    #社員番号1の社員以外について
    for i in range(1, N):
        #直属の上司に1人追加
        ans[A[i] - 1] += 1
    #出力
    for i in range(N):
        print(ans[i])
