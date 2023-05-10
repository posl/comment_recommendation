def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(N-K):
        if A[i] > A[i+K]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()