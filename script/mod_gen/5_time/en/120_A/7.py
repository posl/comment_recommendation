def main():
    A,B,C = map(int,input().split())
    if A <= B:
        if B <= C:
            print(B//A)
        else:
            print(C//A)
    else:
        print(0)

if __name__ == '__main__':
    main()