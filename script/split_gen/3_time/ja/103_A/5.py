def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    ans = A[1] - A[0]
    # 出力
    print(ans)
