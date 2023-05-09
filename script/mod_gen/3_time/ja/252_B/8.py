def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    B.reverse()
    for i in range(K):
        if A[N-1] < B[i]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()