def main():
    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 2つのリストをソートする
    A.sort()
    B.sort()
    # 2つのリストの要素を比較し、
    # どちらかのリストの要素がもう一方のリストの要素より小さい場合は No を出力し、
    # どちらのリストの要素ももう一方のリストの要素より大きい場合は Yes を出力する
    for i in range(M):
        if A[i] < B[i]:
            print("No")
            return
    print("Yes")
