def main():
    N = int(input())
    ans = 0
    for p in range(2, int(N ** 0.5) + 1):
        if N < p * p * p:
            break
        q = 2
        while True:
            k = p * q * q * q
            if N < k:
                break
            ans += 1
            q += 1
    print(ans)
