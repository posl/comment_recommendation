def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    # A[i]の下位60bitの各bitについて、そのbitが立っている数を数える
    # その数がbitが立っている数を数える
    # その数がbitが立っている数を数える
    bit_count = [0] * 60
    for a in A:
        for i in range(60):
            if a >> i & 1:
                bit_count[i] += 1
    # bit_count[i]が立っている数を数える
    # その数がbitが立っている数を数える
    # その数がbitが立っている数を数える
    ans = 0
    for i in range(60):
        ans += (1 << i) * bit_count[i] * (N - bit_count[i])
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()