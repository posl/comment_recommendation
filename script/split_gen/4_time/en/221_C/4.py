def solve():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    max_prod = 0
    for i in range(1, n_len):
        n1 = int(n_str[:i])
        n2 = int(n_str[i:])
        prod = n1 * n2
        if prod > max_prod:
            max_prod = prod
    print(max_prod)
