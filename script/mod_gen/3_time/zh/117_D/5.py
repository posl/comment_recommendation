def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k_bin = bin(k)[2:]
    n_bin = len(k_bin)
    a_bin = [bin(ai)[2:].zfill(n_bin) for ai in a]
    a_bin_t = list(zip(*a_bin))
    a_bin_t = [list(a_bin_ti) for a_bin_ti in a_bin_t]
    a_bin_t.reverse()
    k_bin = list(k_bin)
    k_bin.reverse()
    a_bin_t_max = []
    for i in range(n_bin):
        if k_bin[i] == '0':
            a_bin_t_max.append('1')
        else:
            a_bin_t_max.append(max(a_bin_t[i]))
    a_bin_t_max.reverse()
    a_bin_max = ''.join(a_bin_t_max)
    a_max = int(a_bin_max, 2)
    f_max = 0
    for ai in a:
        f_max += ai ^ a_max
    print(f_max)
main()
