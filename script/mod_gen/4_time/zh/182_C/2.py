def main():
    N = int(input())
    if N % 3 == 0:
        print(0)
        return
    elif N % 3 == 1:
        if N % 10 == 1 and len(str(N)) > 1:
            print(1)
            return
        elif N % 10 == 4 and len(str(N)) > 1:
            print(1)
            return
        elif N % 10 == 7 and len(str(N)) > 1:
            print(1)
            return
        else:
            print(-1)
            return
    else:
        if N % 10 == 2 and len(str(N)) > 1:
            print(1)
            return
        elif N % 10 == 5 and len(str(N)) > 1:
            print(1)
            return
        elif N % 10 == 8 and len(str(N)) > 1:
            print(1)
            return
        else:
            print(-1)
            return

if __name__ == '__main__':
    main()