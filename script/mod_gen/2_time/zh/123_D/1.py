def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(B)
    #print(C)
    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i]+B[j])
    #print(AB)
    AB.sort(reverse=True)
    #print(AB)
    ABC = []
    for i in range(min(K,X*Y)):
        for j in range(Z):
            ABC.append(AB[i]+C[j])
    #print(ABC)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

if __name__ == '__main__':
    main()