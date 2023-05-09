def solve():
    # === 数値を取得 ===
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # === 処理 ===
    # おいしさが最大の食品を取得
    A_max = max(A)
    # 嫌いな食品が含まれているか判定
    for i in range(K):
        if A_max == A[B[i]-1]:
            print("Yes")
            exit()
    # 嫌いな食品が含まれていない場合
    print("No")

if __name__ == '__main__':
    solve()