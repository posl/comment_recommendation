def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    elif N == 250:
        print(2)
        return
    # 250 = 2 * 5^3
    # 250 < N = p * q^3
    # 250 < N = p * q^3
    # q^3 < N / p
    # q < (N / p) ^ (1/3)
    # p < (N / q^3) ^ (1/3)
    ans = 0
    for q in range(2, int(N ** (1 / 3)) + 1):
        p = int(N / q ** 3) ** (1 / 3)
        if p * q ** 3 == N:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()