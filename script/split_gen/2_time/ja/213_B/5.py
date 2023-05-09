def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. スコアが小さい順にソート
    A.sort()
    # 2. 2番目のスコアを出力
    print(A[1])
