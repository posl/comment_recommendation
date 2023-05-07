def main():
    N,K,D = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    A.sort()
    A = A[::-1]
    #print(A)
    S = set()
    for i in range(K):
        for j in range(i+1,K):
            S.add(A[i]+A[j])
    #print(S)
    if(len(S)==0):
        print(-1)
    else:
        S = list(S)
        S.sort()
        S = S[::-1]
        for i in S:
            if(i%D==0):
                print(i)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()