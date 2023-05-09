def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        k = 0
        while 2**k <= N:
            k += 1
        print(k-1)

if __name__ == '__main__':
    main()