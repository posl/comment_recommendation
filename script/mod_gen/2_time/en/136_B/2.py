def main():
    N = int(input())
    if N < 10:
        print(N)
    elif N < 100:
        print(9)
    elif N < 1000:
        print(9 + 1)
    elif N < 10000:
        print(9 + 2)
    elif N < 100000:
        print(9 + 3)
    else:
        print(9 + 4)

if __name__ == '__main__':
    main()