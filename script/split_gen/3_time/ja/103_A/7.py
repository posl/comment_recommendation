def main():
    # 入力
    A = list(map(int, input().split()))
    # 出力
    print(min(A[2]-A[0], A[1]-A[0], A[1]-A[2]))
