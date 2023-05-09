def main():
    N = int(input())
    a = 2
    b = 2
    unrep = 0
    while a < N:
        while b < N:
            if a**b > N:
                break
            unrep += 1
            b += 1
        a += 1
        b = 2
    print(N-unrep)
main()

if __name__ == '__main__':
    main()