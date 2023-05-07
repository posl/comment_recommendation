def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # Aの最大値を求める
    max_a = max(A)
    # Aの最大値のindexを求める
    max_a_index = A.index(max_a)
    # Aの最大値を除いたリストを作る
    A.remove(max_a)
    # Aの最大値を除いたリストの最大値を求める
    max_a2 = max(A)
    # Aの最大値を除いたリストの最大値を出力する
    for i in range(N):
        if i == max_a_index:
            print(max_a2)
        else:
            print(max_a)
