def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    if N == 250:
        print(2)
        return
    ans = 0
    # k = p * q^3
    # k = p * (q^2 * q)
    # k = p * (q^2) * (q)
    for p in range(2, N):
        for q in range(2, N):
            k = p * q**3
            if k > N:
                break
            ans += 1
    print(ans)
