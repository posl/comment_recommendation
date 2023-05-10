def main():
    n = int(input())
    if n < 1000:
        print(0)
        return
    result = 0
    n = str(n)
    n_len = len(n)
    if n_len > 3:
        for i in range(1, n_len):
            result += (10 ** i - 10 ** (i - 1)) * (i // 3)
        result += (int(n) - 10 ** (n_len - 1) + 1) * (n_len // 3)
    print(result)

if __name__ == '__main__':
    main()