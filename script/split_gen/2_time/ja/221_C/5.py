def main():
    N = input()
    N_len = len(N)
    ans = 0
    for i in range(1, 2**N_len):
        A = []
        B = []
        for j in range(N_len):
            if i & (1 << j):
                A.append(N[j])
            else:
                B.append(N[j])
        A.sort(reverse=True)
        B.sort(reverse=True)
        A_num = int(''.join(A))
        B_num = int(''.join(B))
        ans = max(ans, A_num * B_num)
    print(ans)
