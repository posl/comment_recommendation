def main():
    #入力
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    #初期化
    ans = 0
    #処理
    for i in range(N):
        ans += (AB[i][1] - AB[i][0] + 1) * (AB[i][0] + AB[i][1]) // 2
    #出力
    print(ans % (10 ** 9 + 7))
