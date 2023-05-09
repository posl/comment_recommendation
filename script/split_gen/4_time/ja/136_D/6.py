def main():
    # データ入力
    S = input()
    # 計算
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if S[i + 1] == 'R':
                ans[i + 2] += ans[i] + 1
                ans[i] = 0
            else:
                ans[i + 1] += ans[i] + 1
                ans[i] = 0
        else:
            if S[i - 1] == 'L':
                ans[i - 2] += ans[i] + 1
                ans[i] = 0
            else:
                ans[i - 1] += ans[i] + 1
                ans[i] = 0
    # データ出力
    print(' '.join(map(str, ans)))
    return
