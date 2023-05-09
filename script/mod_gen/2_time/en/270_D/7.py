def main():
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    A.sort(reverse=True)
    if N == 1:
        print(1)
        return
    elif N == 2:
        print(2)
        return
    else:
        for i in range(K):
            if A[i] == N:
                print(N)
                return
            elif A[i] < N:
                N -= A[i]
            elif A[i] > N:
                continue
    print(N)

if __name__ == '__main__':
    main()