def main():
    # 標準入力受け取り
    S = input()
    # 処理
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        elif S[i] == '-':
            ans -= 1
    # 出力
    print(ans)
