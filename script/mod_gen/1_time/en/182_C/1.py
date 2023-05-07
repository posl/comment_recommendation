def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sum(N)
    if N % 3 == 0:
        print(0)
    elif len(N) == 1:
        print(-1)
    else:
        if N % 3 == 1:
            if 1 in N or 4 in N or 7 in N:
                print(1)
            elif 2 in N or 5 in N or 8 in N:
                print(2)
            else:
                print(-1)
        elif N % 3 == 2:
            if 2 in N or 5 in N or 8 in N:
                print(1)
            elif 1 in N or 4 in N or 7 in N:
                print(2)
            else:
                print(-1)

if __name__ == '__main__':
    main()