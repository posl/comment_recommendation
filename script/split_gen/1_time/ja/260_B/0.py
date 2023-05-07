def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A_sorted = sorted(A, reverse=True)
    B_sorted = sorted(B, reverse=True)
    C_sorted = sorted(C, reverse=True)
    A_pass = A_sorted[:X]
    B_pass = []
    for b in B_sorted:
        if len(B_pass) == Y:
            break
        if b not in A_pass:
            B_pass.append(b)
    C_pass = []
    for c in C_sorted:
        if len(C_pass) == Z:
            break
        if c not in A_pass and c not in B_pass:
            C_pass.append(c)
    pass_list = A_pass + B_pass + C_pass
    pass_list_sorted = sorted(pass_list, reverse=True)
    for p in pass_list_sorted:
        print(A.index(p) + 1)
