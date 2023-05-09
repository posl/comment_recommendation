def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # 1. Aの最大値を取得する
    max_A = max(A)
    # 2. Aの最大値を除くAの最大値を取得する
    A.remove(max_A)
    max_A2 = max(A)
    # 3. Aの各要素を最大値と比較する
    for i in range(N):
        if A[i] == max_A:
            print(max_A2)
        else:
            print(max_A)
