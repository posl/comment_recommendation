def main():
    n, a, b = map(int, input().split())
    if n < 2 * 10 ** 5:
        ans = pow(2, n, 10 ** 9 + 7) - 1
        ans -= comb(n, a)
        ans -= comb(n, b)
        print(ans % (10 ** 9 + 7))
    else:
        pass

if __name__ == '__main__':
    main()