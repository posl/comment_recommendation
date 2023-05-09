def main():
    N = int(input())
    #N = 1000000000000000000
    #N = 1
    #N = 6
    k = 0
    while 2**k <= N:
        k += 1
    k -= 1
    print(k)

if __name__ == '__main__':
    main()