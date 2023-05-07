def main():
    A,B,C,X = map(int,input().split())
    if X < A:
        print(0)
    elif A <= X <= B:
        print((C/(B-A+1)))
    else:
        print(1)

if __name__ == '__main__':
    main()