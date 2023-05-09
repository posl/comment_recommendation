def main():
    N = int(input())
    k = len(str(N))
    sum = 0
    for i in range(k):
        sum += (N // (10 ** i)) % 10
    if sum % 3 == 0:
        print(0)
    elif k == 1:
        print(-1)
    elif sum % 3 == 1:
        if N % 10 == 1 or N % 10 == 4 or N % 10 == 7:
            print(1)
        elif k == 2:
            print(-1)
        elif N % 100 == 13 or N % 100 == 16 or N % 100 == 19 or N % 100 == 46 or N % 100 == 49 or N % 100 == 79:
            print(2)
        else:
            print(-1)
    else:
        if N % 10 == 2 or N % 10 == 5 or N % 10 == 8:
            print(1)
        elif k == 2:
            print(-1)
        elif N % 100 == 23 or N % 100 == 26 or N % 100 == 29 or N % 100 == 53 or N % 100 == 56 or N % 100 == 59 or N % 100 == 83 or N % 100 == 86 or N % 100 == 89:
            print(2)
        else:
            print(-1)

if __name__ == '__main__':
    main()