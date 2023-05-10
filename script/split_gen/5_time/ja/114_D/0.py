def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    # 素因数分解
    primes = []
    for i in range(2, n + 1):
        for j in range(2, i + 1):
            while i % j == 0:
                primes.append(j)
                i //= j
    # 75の約数を作る
    divs = [1]
    for p in primes:
        divs2 = divs[:]
        for d in divs2:
            divs.append(d * p)
    # 75の約数のうち、n!の約数の個数を数える
    ans = 0
    for d in divs:
        if d == 1:
            continue
        t = n
        while t % d == 0:
            ans += 1
            t //= d
    print(ans)
