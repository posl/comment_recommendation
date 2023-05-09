def main():
    #input
    A,B,C,X = map(int, input().split())
    #output
    if X < A:
        print(0)
    elif A <= X <= B:
        print(1)
    else:
        print((C)/(B-A+1))

if __name__ == '__main__':
    main()