def main():
    N = input()
    N = [int(i) for i in N]
    if sum(N) % 3 == 0:
        print(0)
        return
    if len(N) == 1:
        print(-1)
        return
    if len(N) == 2:
        if (N[0] + N[1]) % 3 == 0:
            print(1)
            return
        else:
            print(-1)
            return
    if len(N) == 3:
        if (N[0] + N[1] + N[2]) % 3 == 0:
            print(0)
            return
        elif (N[0] + N[1]) % 3 == 0 or (N[1] + N[2]) % 3 == 0:
            print(1)
            return
        elif (N[0] + N[2]) % 3 == 0:
            print(2)
            return
        else:
            print(-1)
            return
    if len(N) == 4:
        if (N[0] + N[1] + N[2] + N[3]) % 3 == 0:
            print(0)
            return
        elif (N[0] + N[1] + N[2]) % 3 == 0 or (N[1] + N[2] + N[3]) % 3 == 0:
            print(1)
            return
        elif (N[0] + N[1]) % 3 == 0 or (N[1] + N[2]) % 3 == 0 or (N[2] + N[3]) % 3 == 0:
            print(2)
            return
        elif (N[0] + N[2]) % 3 == 0 or (N[1] + N[3]) % 3 == 0:
            print(3)
            return
        elif (N[0] + N[3]) % 3 == 0:
            print(4)
            return
        else:
            print(-1)
            return
    if len(N) == 5:
        if (N[0] + N[1] + N[2] + N[3]

if __name__ == '__main__':
    main()