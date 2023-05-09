def main():
    N = int(input())
    #N = 963761198400
    #N = 1000000000000
    #N = 12
    #N = 1
    i = 1
    n = 0
    while True:
        if N <= i:
            break
        n += 1
        i += n
    print(n)

if __name__ == '__main__':
    main()