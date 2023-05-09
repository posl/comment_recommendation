def get_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    # 素数判定用
    data = [i + 1 for i in range(2, n)]
    # 素数リスト
    prime = []
    while True:
        p = data[0]
        if p * p > n:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
