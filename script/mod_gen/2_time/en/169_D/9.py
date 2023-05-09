def main():
    N = int(input())
    z = 1
    while N % 2 == 0:
        N //= 2
        z *= 2
    i = 3
    while i * i <= N:
        while N % i == 0:
            N //= i
            z *= i
        i += 2
    if N != 1:
        z *= N
    print(z)

if __name__ == '__main__':
    main()