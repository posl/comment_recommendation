def main():
    n = int(input())
    k = 0
    while True:
        if n < 2**k:
            break
        k += 1
    print(k-1)

if __name__ == '__main__':
    main()