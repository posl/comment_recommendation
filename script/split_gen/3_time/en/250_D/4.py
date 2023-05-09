def main():
    N = int(input())
    ans = 0
    for p in range(2, int(N ** 0.5) + 1):
        if p * p * p > N:
            break
        q = p + 1
        while p * q * q * q <= N:
            ans += 1
            q += 1
    print(ans)
