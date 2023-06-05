def main():
    N,K=map(int,input().split())
    R,S,P=map(int,input().split())
    T=input()
    score=0
    for i in range(N):
        if T[i]=='r':
            if i-K>=0 and T[i-K]=='p':
                T[i]='x'
            else:
                score+=R
        elif T[i]=='s':
            if i-K>=0 and T[i-K]=='r':
                T[i]='x'
            else:
                score+=S
        elif T[i]=='p':
            if i-K>=0 and T[i-K]=='s':
                T[i]='x'
            else:
                score+=P
    print(score)

if __name__ == '__main__':
    main()