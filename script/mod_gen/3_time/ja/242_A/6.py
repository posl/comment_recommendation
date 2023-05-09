def main():
    A,B,C,X = [int(x) for x in input().split()]
    if X <= A:
        print(1)
    elif A < X <= A+C:
        print((C+1)/(B-A+1))
    else:
        print(0)

if __name__ == '__main__':
    main()