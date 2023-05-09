def main():
    # 入力
    S = input()
    # 初期値
    ans = 0
    # 計算
    for i in range(len(S)):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    # 出力
    print(ans)
