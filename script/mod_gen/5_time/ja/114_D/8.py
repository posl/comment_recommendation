def prime_factorize(n):
    # 素因数分解
    # 素因数を要素とするリストを返す
    # 例: 12 -> [2, 2, 3]
    # 計算量: O(√n)
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n = int(input())

if __name__ == '__main__':
    prime_factorize()