def main():
    # 入力
    N = int(input())
    W = list(map(int, input().split()))
    # 処理
    min = 1000
    for i in range(1, N):
        W1 = sum(W[:i])
        W2 = sum(W[i:])
        if abs(W1 - W2) < min:
            min = abs(W1 - W2)
    # 出力
    print(min)
