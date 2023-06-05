def main():
    N = int(input())
    k = 0
    while True:
        if 2**k > N:
            break
        k += 1
    print(k-1)

if __name__ == '__main__':
    main()