def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #Aの最大値を取得
    maxA = max(A)
    #Aの最大値を超える数値を格納
    overA = []
    #Aの最大値を超える数値を格納
    for i in range(1, maxA + 1):
        if i not in A:
            overA.append(i)
    #Aの最大値を超える数値の個数を取得
    overA_num = len(overA)
    #Aの最大値を超える数値の個数がK以下の場合
    if overA_num <= K:
        print(overA_num)
    #Aの最大値を超える数値の個数がKより大きい場合
    else:
        print(K)
