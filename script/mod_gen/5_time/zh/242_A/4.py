def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X >= A+1 and X <= B:
        print(C/(B-A))
    else:
        print(0)

if __name__ == '__main__':
    main()