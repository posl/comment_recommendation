def main():
    N = int(input())
    N_sqrt = int(N**0.5)
    divisors = []
    for i in range(1, N_sqrt+1):
        if N % i == 0:
            print(i)
            if i != N // i:
                divisors.append(N // i)
    for i in reversed(divisors):
        print(i)

if __name__ == '__main__':
    main()