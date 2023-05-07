def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    ans = 0
    for p in range(2, int(N**0.5)+1):
        if N % p == 0:
            e = 0
            while N % p == 0:
                N //= p
                e += 1
            ans += e
    if N != 1:
        ans += 1
    print(ans)
