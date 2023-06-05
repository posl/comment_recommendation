def get_max_product(n):
    l = len(n)
    if l == 2:
        return int(n[0])*int(n[1])
    else:
        max_product = 0
        for i in range(1, l):
            n1 = n[:i]
            n2 = n[i:]
            if n1[0] != '0' and n2[0] != '0':
                product = int(n1)*int(n2)
                if max_product < product:
                    max_product = product
        return max_product

if __name__ == '__main__':
    get_max_product()