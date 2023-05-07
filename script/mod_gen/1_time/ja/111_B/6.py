def main():
    N = int(input())
    n = 1
    while True:
        if n > N:
            break
        n *= 10
    n //= 10
    ans = N // n * n + n - 1
    print(ans)

if __name__ == '__main__':
    main()