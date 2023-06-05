def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        print("Yes")
    else:
        for i in range(K-1):
            if A[i] > A[i+1]:
                print("No")
                exit()
        for i in range(K-1, N-1):
            if A[i] > A[i+1]:
                print("Yes")
                exit()
        print("No")

if __name__ == '__main__':
    main()