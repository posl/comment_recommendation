def main():
    N = input()
    N = N[::-1]
    N = [int(i) for i in N]
    if sum(N)%3 == 0:
        print(0)
    elif len(N) == 1:
        print(-1)
    elif len(N) == 2:
        if (N[0] + N[1])%3 == 0:
            print(1)
        else:
            print(-1)
    else:
        if sum(N)%3 == 1:
            if 1 in N:
                print(1)
            elif 4 in N:
                print(1)
            elif 7 in N:
                print(1)
            elif 2 in N and 5 in N:
                print(2)
            elif 2 in N and 8 in N:
                print(2)
            elif 5 in N and 8 in N:
                print(2)
            else:
                print(-1)
        else:
            if 2 in N:
                print(1)
            elif 5 in N:
                print(1)
            elif 8 in N:
                print(1)
            elif 1 in N and 4 in N:
                print(2)
            elif 1 in N and 7 in N:
                print(2)
            elif 4 in N and 7 in N:
                print(2)
            else:
                print(-1)

if __name__ == '__main__':
    main()