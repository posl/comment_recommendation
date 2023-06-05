def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        print(1/C)
    else:
        print(0.0)

if __name__ == '__main__':
    main()