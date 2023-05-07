def main():
    X = input()
    M = int(input())
    X = list(map(int, X))
    X.sort()
    X.reverse()
    d = X[0]
    # d+1以上の最小のnを求める
    n = d+1
    while True:
        if n**len(X) > M:
            break
        n += 1
    # n進法で表現したときの最小の値を求める
    min_n = 0
    for i in range(len(X)):
        min_n += X[i] * (n**i)
    # n進法で表現したときの最大の値を求める
    max_n = 0
    for i in range(len(X)):
        max_n += X[i] * (n**(len(X)-i-1))
    # 最小の値がM以下の場合、答えは1
    if min_n <= M:
        print(1)
        return
    # Mがn進法で表現したときの最小の値と最大の値の間にある場合、答えは2
    if min_n <= M and M <= max_n:
        print(2)
        return
    # Mがn進法で表現したときの最大の値より大きい場合、答えは0
    if M < min_n:
        print(0)
        return
