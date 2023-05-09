def main():
    # 入力
    S = input()
    N = len(S)
    # 計算
    count = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    # 出力
    print(count)
