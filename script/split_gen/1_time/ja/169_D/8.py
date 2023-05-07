def main():
    N = int(input())
    # 素数を列挙
    prime = []
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            prime.append(i)
            while N % i == 0:
                N //= i
    if N != 1:
        prime.append(N)
    # 素因数分解
    ans = 0
    for p in prime:
        e = 1
        while p**e <= N:
            e += 1
        ans += e - 1
    print(ans)
