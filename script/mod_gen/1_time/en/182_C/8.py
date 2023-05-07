def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    #print(N)
    #print(sum(N))
    if sum(N)%3 == 0:
        print(0)
        exit()
    if len(N) == 1:
        print(-1)
        exit()
    if len(N) == 2:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            print(-1)
            exit()
    if len(N) == 3:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            print(1)
            exit()
    if len(N) == 4:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            if N[0]%3 == 0 or N[1]%3 == 0 or N[2]%3 == 0 or N[3]%3 == 0:
                print(1)
                exit()
            else:
                print(-1)
                exit()
    if len(N) == 5:
        if sum(N)%3 == 0:
            print(0)
            exit()
        else:
            if N[0]%3 == 0 or N[1]%3 == 0 or N[2]%3 == 0 or N[3]%3 == 0 or N[4]%3 == 0:
                print(1)
                exit()
            else:
                if (N[0] + N[1])%3 == 0 or (N[0] + N[2])%3 == 0 or (N[0] + N[3])%3 == 0 or (N[0] + N[4])%3 == 0 or (N[1] + N[2])%3 == 0 or (N[1] + N[3])%3 == 0 or (N[1] + N[4])%3 == 0 or (N[2] + N[3])%3 == 0 or (N[2] + N[4])%3 == 0 or (N[3] + N[4])%3 == 0:
                    print(2)
                    exit()
                else:
                    print(-1)

if __name__ == '__main__':
    main()