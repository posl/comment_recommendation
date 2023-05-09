def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    T %= S
    for i in range(N):
        if T < A[i]:
            print(i+1, T)
            break
        else:
            T -= A[i]

if __name__ == '__main__':
    main()