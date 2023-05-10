def main():
    # データ入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # データ整理
    A.sort()
    # 並び替え可能かどうかの判定
    for i in range(N-K):
        if A[i] == A[i+K]:
            print("Yes")
            exit()
    print("No")
