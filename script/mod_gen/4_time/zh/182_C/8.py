def main():
    N = int(input())
    if N % 3 == 0:
        print(0)
        return
    N = list(str(N))
    N = [int(n) for n in N]
    N.sort()
    if N[0] == 1 or N[0] == 4 or N[0] == 7:
        if len(N) == 1:
            print(-1)
            return
        if N[1] == 2 or N[1] == 5 or N[1] == 8:
            print(2)
            return
        else:
            print(1)
            return
    elif N[0] == 2 or N[0] == 5 or N[0] == 8:
        if len(N) == 1:
            print(-1)
            return
        if N[1] == 1 or N[1] == 4 or N[1] == 7:
            print(2)
            return
        else:
            print(1)
            return
    else:
        print(-1)
        return

if __name__ == '__main__':
    main()