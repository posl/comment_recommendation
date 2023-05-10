def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    for i in range(N):
        if abs(A[i]-B[i])>K:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()