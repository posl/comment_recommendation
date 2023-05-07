def main():
    # 入力
    N, K = map(int, input().split())
    S = input()
    # 連続するLの数を保持する配列
    L = []
    # 連続するRの数を保持する配列
    R = []
    # 連続するLの数を数える
    count = 0
    for i in range(N):
        if S[i] == "L":
            count += 1
        else:
            L.append(count)
            count = 0
    L.append(count)
    # 連続するRの数を数える
    count = 0
    for i in range(N):
        if S[N-i-1] == "R":
            count += 1
        else:
            R.append(count)
            count = 0
    R.append(count)
    # Rの数が多い順にソート
    R.sort(reverse=True)
    # 操作
    ans = 0
    for i in range(min(K, len(R))):
        ans += R[i]
    # 連続するLの数が偶数の場合、幸福な人数を増やす
    for i in range(len(L)):
        if L[i] % 2 == 0:
            ans += L[i]
    # 出力
    print(ans)
