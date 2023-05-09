def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    N_loop = T // A_sum
    T_mod = T % A_sum
    for i in range(N):
        if T_mod < A[i]:
            print(i + 1, T_mod)
            break
        else:
            T_mod -= A[i]

if __name__ == '__main__':
    main()