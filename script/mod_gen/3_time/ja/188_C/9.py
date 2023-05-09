def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2N人の選手について、勝利したかどうかを記録するリストを作成
    win = [0] * (2**N)
    for i in range(N):
        # 対戦の順序を記録するリストを作成
        order = []
        for j in range(2**(N-i)):
            # まだ勝利していない選手のうち、レートが高いほうを勝利とする
            if A[2*j] > A[2*j+1]:
                win[2*j] = 1
                order.append(2*j)
            else:
                win[2*j+1] = 1
                order.append(2*j+1)
        # 次の対戦のために、対戦順序を記録したリストを元に、
        # Aの要素を更新する
        for j in range(2**(N-i)):
            A[j] = A[order[j]]
    # 最後に負けた選手の番号を出力
    print(A.index(min(A))+1)

if __name__ == '__main__':
    main()