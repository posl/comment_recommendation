def main():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()