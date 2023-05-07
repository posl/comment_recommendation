def main():
    N, M, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N, M, X, Y)
    #print(A)
    #print(B)
    
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    
    for i in range(X, Y+1):
        if A[-1] < i and i <= B[0]:
            print("No War")
            exit()
    print("War")

if __name__ == '__main__':
    main()