def main():
    A,B,K = map(int,input().split())
    if A>=K:
        A-=K
    else:
        K-=A
        A=0
        B-=K
        if B<0:
            B=0
    print(A,B)

if __name__ == '__main__':
    main()