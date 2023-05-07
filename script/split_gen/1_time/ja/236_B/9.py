def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #カードの枚数を数える
    card = [0] * (N+1)
    for i in range(4*N-1):
        card[A[i]] += 1
    #カードの枚数が奇数のものを出力
    for i in range(1, N+1):
        if card[i] % 2 == 1:
            print(i)
