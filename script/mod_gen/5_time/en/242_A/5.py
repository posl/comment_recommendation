def main():
    A, B, C, X = map(int, input().split())
    #print(A, B, C, X)
    if A >= X:
        print(1)
    elif A + C >= X:
        print(C / (B - A + 1))
    else:
        print(0)

if __name__ == '__main__':
    main()