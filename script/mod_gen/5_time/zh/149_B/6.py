def main():
    A,B,K = map(int,input().split())
    if K == 0:
        print(A,B)
    else:
        if A >= K:
            print(A-K,B)
        else:
            if A+B >= K:
                print(0,B-(K-A))
            else:
                print(0,0)

if __name__ == '__main__':
    main()