def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    bit = [0] * 41
    for a in A:
        for i in range(41):
            if a & (1 << i):
                bit[i] += 1
    ans = 0
    for i in range(41):
        if bit[40 - i] < N - bit[40 - i]:
            ans += (1 << (40 - i)) * (N - bit[40 - i])
        else:
            ans += (1 << (40 - i)) * bit[40 - i]
    print(ans)

if __name__ == '__main__':
    main()