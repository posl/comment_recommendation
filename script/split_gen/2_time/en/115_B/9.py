def main():
    #入力
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    #ソート
    p_list.sort()
    #最大値を半額にする
    p_list[-1] = p_list[-1] / 2
    #合計
    ans = sum(p_list)
    #出力
    print(int(ans))
main()
