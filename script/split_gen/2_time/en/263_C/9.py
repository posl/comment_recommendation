def gen_inc_seq(n, m, seq):
    if n == 0:
        print(*seq)
        return
    for i in range(1, m+1):
        if len(seq) == 0 or seq[-1] < i:
            seq.append(i)
            gen_inc_seq(n-1, m, seq)
            seq.pop()
n, m = map(int, input().split())
gen_inc_seq(n, m, [])
