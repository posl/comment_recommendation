def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X >= B:
        print(0)
    else:
        print(C/(B-A))

if __name__ == '__main__':
    main()