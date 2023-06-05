def harvest_nuts(num_nuts):
    nuts = []
    for i in range(num_nuts):
        nuts.append(int(input()))
    nuts.sort()
    nuts.reverse()
    total_nuts = 0
    for i in range(num_nuts):
        if nuts[i] >= 10:
            total_nuts += nuts[i] - 10
    return total_nuts
