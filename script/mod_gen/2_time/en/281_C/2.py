def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    mod_T = T % sum_A
    if mod_T == 0:
        print(N, A[-1])
    else:
        for i in range(N):
            if mod_T - A[i] <= 0:
                print(i + 1, mod_T)
                break
            else:
                mod_T -= A[i]

if __name__ == '__main__':
    main()