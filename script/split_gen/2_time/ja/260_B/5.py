def main():
    # 入力
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 処理
    C = [A[i] + B[i] for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    A_pass = A[:X]
    B_pass = B[:Y]
    C_pass = C[:Z]
    A_pass.extend(B_pass)
    A_pass.extend(C_pass)
    A_pass = list(set(A_pass))
    A_pass.sort()
    # 出力
    for i in range(len(A_pass)):
        print(A_pass[i])
