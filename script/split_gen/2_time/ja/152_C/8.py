def main():
    N = int(input())
    P = list(map(int, input().split()))
    # Pの最小値を求める
    min_P = P[0]
    for i in range(1, N):
        if P[i] < min_P:
            min_P = P[i]
    # Pの最小値を含む連続した部分列の長さを求める
    count = 1
    for i in range(1, N):
        if P[i] < min_P:
            break
        else:
            count += 1
    # Pの最小値を含む連続した部分列の長さを出力する
    print(count)
