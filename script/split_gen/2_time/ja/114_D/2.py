def divisor(n):
    # 約数を列挙する
    d = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.append(i)
            if n // i != i:
                d.append(n // i)
    return d
