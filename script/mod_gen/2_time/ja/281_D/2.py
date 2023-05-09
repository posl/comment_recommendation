def main():
    N,K,D=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    S=set()
    for i in range(N):
        for j in range(i+1,N):
            S.add(A[i]+A[j])
    S=list(S)
    S.sort()
    if len(S)<K:
        print(-1)
    else:
        print(S[-K])
main()

if __name__ == '__main__':
    main()