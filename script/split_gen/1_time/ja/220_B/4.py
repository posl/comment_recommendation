def main():
    # 入力
    K = int(input())
    A, B = input().split()
    # 処理
    A10 = int(A, K)
    B10 = int(B, K)
    C10 = A10 * B10
    # 出力
    print(C10)
