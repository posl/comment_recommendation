def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    max_product = 0
    for i in range(1, n_len):
        max_product = max(max_product, int(n_str[:i]) * int(n_str[i:]))
    print(max_product)

if __name__ == '__main__':
    main()