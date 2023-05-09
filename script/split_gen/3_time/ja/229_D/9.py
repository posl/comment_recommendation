def main():
    S = input()
    K = int(input())
    N = len(S)
    # X が連続する部分をまとめる
    X = []
    cnt = 0
    for i in range(N):
        if S[i] == "X":
            cnt += 1
        else:
            if cnt > 0:
                X.append(cnt)
            cnt = 0
    if cnt > 0:
        X.append(cnt)
    # X が連続する部分のうち、K 個以上連続する部分を削除する
    M = len(X)
    for i in range(M):
        if X[i] <= K:
            K -= X[i]
            X[i] = 0
        else:
            X[i] -= K
            break
    # X が連続する部分の長さの和が答え
    ans = sum(X)
    print(ans)
