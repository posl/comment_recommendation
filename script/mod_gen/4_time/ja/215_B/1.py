def main():
    N = int(input())
    k = 0
    while True:
        if 2**k <= N:
            k += 1
        else:
            break
    print(k-1)

if __name__ == '__main__':
    main()