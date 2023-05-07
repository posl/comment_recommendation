def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    count = T // sum_A
    T = T - (sum_A * count)
    for i in range(N):
        if T - A[i] <= 0:
            print(i+1, T)
            break
        else:
            T -= A[i]

if __name__ == '__main__':
    main()