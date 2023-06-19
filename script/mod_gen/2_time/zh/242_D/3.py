def main():
    S=input()
    Q=int(input())
    for i in range(Q):
        t,k=map(int,input().split())
        t=t%(3*10**18)
        for j in range(t):
            S=S.replace('a','bc')
            S=S.replace('b','ca')
            S=S.replace('c','ab')
        print(S[k-1])

if __name__ == '__main__':
    main()