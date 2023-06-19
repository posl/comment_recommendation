def main():
    A,B,K = map(int,input().split())
    if K == 0:
        print(A,B)
    elif A == 0:
        print(0,B-K)
    elif B == 0:
        print(A-K,0)
    elif A+B <= K:
        print(0,0)
    elif A <= K:
        print(0,B-(K-A))
    else:
        print(A-K,B)

if __name__ == '__main__':
    main()