def findMaxProduct(N):
    N_str = str(N)
    N_len = len(N_str)
    max_product = 0
    for i in range(1, N_len):
        N1 = int(N_str[0:i])
        N2 = int(N_str[i:N_len])
        product = N1 * N2
        if product > max_product:
            max_product = product
    return max_product

if __name__ == '__main__':
    findMaxProduct()