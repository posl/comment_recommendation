def main():
    #標準入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aの要素の個数をカウントする
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1
    #countの要素の値を合計する
    total = 0
    for i in range(N+1):
        total += count[i] * (count[i] - 1) // 2
    #出力
    for i in range(N):
        print(total - (count[A[i]] - 1))
