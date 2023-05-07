def main():
    N,K=map(int,input().split())
    P=[list(map(int,input().split())) for _ in range(N)]
    S=[sum(p) for p in P]
    T=[sum(p[:3]) for p in P]
    T.sort()
    for i in range(N):
        if S[i]+T[N-K]<T[N-K-1]+300:
            print("No")
        else:
            print("Yes")
main()

if __name__ == '__main__':
    main()