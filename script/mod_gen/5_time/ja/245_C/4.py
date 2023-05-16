def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # すべての i(1 ≦ i ≦ N) について、X_i = A_i または X_i = B_i
    # すべての i(1 ≦ i ≦ N-1) について、|X_i - X_{i+1}| ≦ K
    # ということは、X_i は A_i と B_i のどちらかの値でなければならない
    # よって、X_i は A_i と B_i のうち、小さい方の値になる
    # すべての i(1 ≦ i ≦ N-1) について、|X_i - X_{i+1}| ≦ K
    # ということは、X_i は X_{i+1} から K 以内の値になる
    # よって、X_i は X_{i+1} から K 以内の値のうち、小さい方の値になる
    # 以上より、X_i は A_i と B_i、X_{i+1} と X_i のうち、小さい方の値になる
    # すなわち、X_i = min(A_i, B_i, X_{i+1}) となる
    # これを全ての i について行えば、X_1, X_2, ..., X_N を求めることができる
    # このとき、X_N は A_N と B_N のうち、小さい方の値になる
    # よって、X_N = min(A_N, B_N) となる
    # 以上より、X_1, X_2, ..., X_N を求めることができる
    # これらの値が条件を満たすか

if __name__ == '__main__':
    solve()