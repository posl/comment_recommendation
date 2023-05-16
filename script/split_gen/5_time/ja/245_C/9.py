def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Xの1番目の要素はA_1またはB_1
    # Xの2番目の要素はA_2またはB_2
    # ...
    # XのN番目の要素はA_NまたはB_N
    # というように、Xのi番目の要素はA_iまたはB_i
    # というように決まっている。
    # このように決まっている数列Xが存在するかどうかを判定する。
    # このように決まっている数列Xが存在するかどうかを判定するには、
    # 以下のように判定すればよい。
    # すべてのi(1 ≦ i ≦ N)について、X_i = A_i または X_i = B_i
    # すべてのi(1 ≦ i ≦ N-1)について、|X_i - X_{i+1}| ≦ K
    # であるかどうかを判定すればよい。
    # ここで、すべてのi(1 ≦ i ≦ N)について、X_i = A_i または X_i = B_i
    # であるかどうかを判定するには、
    # すべてのi(1 ≦ i ≦ N)について、X_i = A_i かつ X_i = B_i
    # であるかどうかを判定すればよい。
    # すべてのi(1 ≦ i ≦ N)について、X_i = A_i かつ X_i = B_i
    # であるかどうかを判定するには、
    # すべてのi(1 ≦ i ≦