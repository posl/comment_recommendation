def main():
    N, K = map(int, input().split())
    S = input()
    # 0 と 1 の間に 1 を挿入して 0 と 1 の数を揃える
    # 0 と 1 の数は K + 1 以下のため、全探索できる
    S = S.replace("01", "0 1").replace("10", "1 0").split()
    # 0 と 1 の数
    num = [0] * (len(S) + 1)
    for i in range(len(S)):
        num[i + 1] = num[i] + int(S[i])
    # 0 と 1 の数の差
    diff = [0] * (len(S) + 1)
    for i in range(len(S)):
        diff[i + 1] = diff[i] + int(S[i]) * 2 - 1
    # 0 と 1 の数の差の最大値
    ans = 0
    for i in range(len(S) + 1):
        for j in range(i, len(S) + 1):
            if num[j] - num[i] <= K:
                ans = max(ans, diff[j] - diff[i])
    print(ans)
