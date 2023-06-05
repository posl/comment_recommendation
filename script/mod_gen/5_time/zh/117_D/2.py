def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k_bin = bin(k)[2:]
    n_bin = len(k_bin)
    a_bin = [bin(a_i)[2:] for a_i in a]
    a_bin = [a_i.zfill(n_bin) for a_i in a_bin]
    a_bin = list(zip(*a_bin))
    a_bin = ["".join(a_i) for a_i in a_bin]
    a_bin = [int(a_i, 2) for a_i in a_bin]
    a_bin = sorted(a_bin, reverse=True)
    k_bin = k_bin.zfill(n_bin)
    k_bin = [int(k_bin_i) for k_bin_i in k_bin]
    k_bin = [k_bin_i * 2 ** (n_bin - 1 - i) for i, k_bin_i in enumerate(k_bin)]
    k_bin = sum(k_bin)
    ans = 0
    for a_i in a_bin:
        if ans + a_i <= k_bin:
            ans += a_i
    print(ans)

if __name__ == '__main__':
    main()