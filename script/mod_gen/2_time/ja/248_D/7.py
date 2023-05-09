def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    #print(N,A,Q)
    #print("-----")
    for i in range(Q):
        L,R,X = map(int, input().split())
        #print(L,R,X)
        print(A[L-1:R].count(X))

if __name__ == '__main__':
    main()