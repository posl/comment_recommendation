def main():
    N,A,B=map(int,input().split())
    P,Q,R,S=map(int,input().split())
    if S<B:
        for i in range(P,Q+1):
            print("."*(S-R+1))
    elif B<=R:
        for i in range(P,Q+1):
            print("#"*(S-R+1))
    else:
        for i in range(P,Q+1):
            if i<A:
                print("#"*(B-R)+"."*(S-B+1))
            elif A<=i<=N-B+1:
                print("#"*(B-R)+"."*(S-B+1))
            else:
                print("."*(B-R)+"#"*(S-B+1))

if __name__ == '__main__':
    main()