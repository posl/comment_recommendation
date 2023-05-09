def main():
    A,B,C,X = map(int,input().split())
    if A >= X:
        print(0)
    elif A < X and X <= B:
        print((C)/(B-A))
    else:
        print(1)

if __name__ == '__main__':
    main()