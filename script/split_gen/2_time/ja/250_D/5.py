def main():
    N = int(input())
    # N以下の素数リスト
    primes = []
    # N以下の素数の平方のリスト
    squares = []
    # N以下の素数の立方のリスト
    cubes = []
    # N以下の素数の四乗のリスト
    quads = []
    # N以下の素数リストの作成
    for i in range(2, N+1):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    # N以下の素数の平方のリストの作成
    for p in primes:
        if p*p <= N:
            squares.append(p*p)
        else:
            break
    # N以下の素数の立方のリストの作成
    for p in primes:
        if p*p*p <= N:
            cubes.append(p*p*p)
        else:
            break
    # N以下の素数の四乗のリストの作成
    for p in primes:
        if p*p*p*p <= N:
            quads.append(p*p*p*p)
        else:
            break
    # 答えの計算
    ans = 0
    for q in quads:
        for c in cubes:
            if q+c <= N:
                ans += 1
            else:
                break
    for s in squares:
        for c in cubes:
            if s+c <= N:
                ans += 1
            else:
                break
    for p in primes:
        for c in cubes:
            if p*c <= N:
                ans += 1
            else:
                break
    print(ans)
