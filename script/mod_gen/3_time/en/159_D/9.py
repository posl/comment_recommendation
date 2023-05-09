def main():
    import sys
    from collections import Counter
    #入力
    readline = sys.stdin.readline
    N = int(readline())
    A = list(map(int, readline().split()))
    #処理
    #Aの要素の個数を数える
    counter = Counter(A)
    #Aの要素の個数をリストにする
    B = list(counter.values())
    #Aの要素の個数の合計を求める
    total = sum(B)
    #Aの要素の個数から2個選ぶ組み合わせの個数を求める
    C = [b*(total-b) for b in B]
    #出力
    for i in range(N):
        print(C[A[i]-1])

if __name__ == '__main__':
    main()