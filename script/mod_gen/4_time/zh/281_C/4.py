def main():
    N,T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    for i in range(N):
        if T <= A[i]:
            print(i+1, T)
            return
        else:
            T -= A[i]

if __name__ == '__main__':
    main()