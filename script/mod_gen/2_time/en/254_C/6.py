def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    for i in range(0, N-K):
        if A[i] > A[i+K]:
            print("Yes")
            return 0
    print("No")

if __name__ == '__main__':
    main()