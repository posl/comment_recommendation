def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n & 1:#偶数
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):#从3开始到根号n,步长为2
        if n % i == 0:
            return False
    return True
