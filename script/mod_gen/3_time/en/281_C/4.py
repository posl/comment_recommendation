def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    count = T // sum_A
    T = T % sum_A
    for i in range(N):
        if T <= A[i]:
            print(i + 1, T)
            break
        T -= A[i]

if __name__ == '__main__':
    main()