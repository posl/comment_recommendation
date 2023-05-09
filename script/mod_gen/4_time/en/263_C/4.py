def rec(i, N, M, seq):
    if i == N:
        print(' '.join(map(str, seq)))
        return
    for j in range(seq[i-1]+1, M+1):
        seq[i] = j
        rec(i+1, N, M, seq)

if __name__ == '__main__':
    rec()