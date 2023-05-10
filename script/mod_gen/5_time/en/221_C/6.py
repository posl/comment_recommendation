def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    ans = 0
    for i in range(1, 2**N_len-1):
        A = []
        B = []
        for j in range(N_len):
            if ((i >> j) & 1):
                A.append(N_str[j])
            else:
                B.append(N_str[j])
        A.sort(reverse=True)
        B.sort(reverse=True)
        A_num = int("".join(A))
        B_num = int("".join(B))
        ans = max(ans, A_num*B_num)
    print(ans)

if __name__ == '__main__':
    main()