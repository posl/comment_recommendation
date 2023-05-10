def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if n <= b:
        print(0)
        return
    if a == b:
        print(1)
        return
    comb = 1
    for i in range(n):
        comb *= (n - i)
        comb %= 1000000007
    for i in range(n - b):
        comb *= pow(i + 1, 1000000005, 1000000007)
        comb %= 1000000007
    for i in range(n - a):
        comb *= pow(i + 1, 1000000005, 1000000007)
        comb %= 1000000007
    print((pow(2, n, 1000000007) - comb - comb) % 1000000007)

if __name__ == '__main__':
    main()