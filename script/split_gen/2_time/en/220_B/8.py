def base_k_to_decimal(x, k):
    x = str(x)
    k = int(k)
    result = 0
    for i in range(len(x)):
        result += int(x[i])*(k**(len(x)-i-1))
    return result
