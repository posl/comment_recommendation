def main():
    S = input()
    K = int(input())
    # 答えを格納する変数
    ans = 0
    # 連続するXの数
    count = 0
    # 連続するXの数をカウント
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            # XとXの間にある.の数を加算
            ans += count - 1 if count > 1 else 0
            count = 0
    # 最後のXとXの間にある.の数を加算
    ans += count - 1 if count > 1 else 0
    # K回操作を行う
    ans += K * 2
    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()