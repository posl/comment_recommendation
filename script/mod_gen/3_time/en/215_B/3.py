def main():
    N = int(input())
    i = 0
    while 2**i <= N:
        i += 1
    print(i-1)

if __name__ == '__main__':
    main()