Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 入力
    X, K = map(int, input().split())

    # 処理
    for i in range(K):
        X = round(X, -i)

    # 出力
    print(X)

=======
Suggestion 2

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = round(X, -i)
    print(X)

=======
Suggestion 3

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X + 5 * 10**i) // (10**i * 10) * 10**i * 10
    print(X)

=======
Suggestion 4

def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = X // 10 ** i * 10 ** i + 10 ** i
    print(X // 10 ** K * 10 ** K)

=======
Suggestion 5

def round_down(num, divisor):
    return num - (num%divisor)

=======
Suggestion 6

def main():
    x,k = map(int,input().split())
    for i in range(k):
        x = round(x,-i)
    print(x)

=======
Suggestion 7

def main():
    x, k = map(int, input().split())
    print(x + (10 ** k - x % (10 ** k)) % (10 ** k))

=======
Suggestion 8

def main():
    X, K = map(int, input().split())
    # X は 10^15 未満の整数
    # K は 1 以上 15 以下の整数
    # X の 10^i の位以下を四捨五入する
    # 10^i の位以下を 0 にする
    # 10^i で割った余りが 5 以上なら 10^i を足す
    # 10^i で割った余りが 5 未満なら何もしない
    # 10^i で割った余りが 5 であれば、さらに 10^i で割った余りが 0 であれば何もしない
    # さらに 10^i で割った余りが 0 でなければ 10^i を足す
    # 10^i で割った余りが 5 であれば、さらに 10^i で割った余りが 0 であれば 10^i を足す
    # 10^i で割った余りが 5 であれば、さらに 10^i で割った余りが 0 であれば何もしない
    # 10^i の位以下を 0 にする
    # 10^i で割った余りが 5 以上なら 10^i を足す
    # 10^i で割った余りが 5 未満なら何もしない
    # 10^i で割った余りが 5 であれば、さらに 10^i で割った余りが 0 であれば何もしない
    # さらに 10^i で割った余りが 0 でなければ 10^i を足す

=======
Suggestion 9

def round(x, k):
    return int(x / (10 ** k)) * (10 ** k)
