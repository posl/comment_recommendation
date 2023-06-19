def main():
    N,M,T = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    if A[0] != 1:
        print("No")
        return
    for i in range(M-1):
        if B[i] != A[i+1]:
            print("No")
            return
    if B[M-1] != T:
        print("No")
        return
    for i in range(M):
        if (B[i] - A[i]) % 2 == 0:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()