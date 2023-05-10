def main():
    N = input()
    if len(N) == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
    elif len(N) == 2:
        if int(N) % 3 == 0:
            print(0)
        elif int(N[0]) % 3 == 0 or int(N[1]) % 3 == 0:
            print(1)
        else:
            print(-1)
    else:
        N = list(N)
        sum = 0
        for i in range(len(N)):
            sum += int(N[i])
        if sum % 3 == 0:
            print(0)
        elif sum % 3 == 1:
            if 1 in N:
                print(1)
            elif 2 in N:
                if N.count(2) >= 2:
                    print(2)
                else:
                    print(-1)
            else:
                print(-1)
        else:
            if 2 in N:
                print(1)
            elif 1 in N:
                if N.count(1) >= 2:
                    print(2)
                else:
                    print(-1)
            else:
                print(-1)

if __name__ == '__main__':
    main()