def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = A[::-1]
    for i in range(N-K):
        if A[i] == B[i]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()