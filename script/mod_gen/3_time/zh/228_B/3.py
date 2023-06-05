def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.insert(0,0)
    B = [0]*(N+1)
    B[X] = 1
    for i in range(1,N+1):
        if B[i] == 1:
            B[A[i]] = 1
    print(B.count(1))

if __name__ == '__main__':
    main()