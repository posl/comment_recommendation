def main():
    # input
    N = int(input())
    # compute
    i = 1
    while True:
        if N <= i*(i+1)/2:
            break
        i += 1
    # output
    print(i)

if __name__ == '__main__':
    main()