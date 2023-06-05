def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        if i ** 2 > N:
            break
        n = N
        while n % i == 0:
            n //= i
        if n % i == 1:
            ans -= 1
        while n % i == 0:
            n //= i
        if n == 1:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()