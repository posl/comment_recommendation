def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 1. 数学の点が高い方から X 人を合格とする。
    A.sort(reverse=True)
    X_list = A[:X]
    #print(X_list)
    # 2. 次に、この時点でまだ合格となっていない受験者のうち、英語の点が高い方から Y 人を合格とする。
    B.sort(reverse=True)
    Y_list = B[:Y]
    #print(Y_list)
    # 3. 次に、この時点でまだ合格となっていない受験者のうち、数学と英語の合計点が高い方から Z 人を合格とする。
    C = [(A[i] + B[i]) for i in range(N)]
    C.sort(reverse=True)
    Z_list = C[:Z]
    #print(Z_list)
    # 4. ここまでで合格となっていない受験者は、不合格とする。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
    # 1. から 3. までのどの段階についても、同点であった場合は受験生の番号の小さい方を優先します。
