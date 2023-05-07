def main():
    #入力
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    #ソート
    A.sort(reverse = True)
    B.sort(reverse = True)
    C.sort(reverse = True)
    
    #計算
    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i] + B[j])
    AB.sort(reverse = True)
    ABC = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            ABC.append(AB[i] + C[j])
    ABC.sort(reverse = True)
    
    #出力
    for i in range(K):
        print(ABC[i])

if __name__ == '__main__':
    main()