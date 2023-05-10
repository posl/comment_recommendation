def main():
    n, k = map(int, input().split())
    if k % 2 == 0:
        n1 = n // k
        n2 = (n + k // 2) // k
        print(n1 ** 3 + n2 ** 3)
    else:
        print((n // k) ** 3)

if __name__ == '__main__':
    main()