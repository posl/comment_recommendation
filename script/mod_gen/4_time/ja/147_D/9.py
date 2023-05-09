def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    #ビットごとに1が立っている数
    bit_count = [0] * 60
    for a in A:
        for bit in range(60):
            if a & (1<<bit):
                bit_count[bit] += 1
    #ビットごとに1が立っている数の組み合わせ
    bit_comb = [0] * 60
    for bit in range(60):
        bit_comb[bit] = bit_count[bit] * (N - bit_count[bit])
    #ビットごとに1が立っている数の組み合わせの和
    bit_sum = 0
    for bit in range(60):
        bit_sum += bit_comb[bit] * (1<<bit)
    print(bit_sum % mod)

if __name__ == '__main__':
    solve()