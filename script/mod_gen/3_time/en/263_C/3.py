def dfs(N,M,seq):
    if len(seq) == N:
        print(' '.join(map(str, seq)))
        return
    for i in range(1,M+1):
        if len(seq) == 0 or seq[-1] < i:
            seq.append(i)
            dfs(N,M,seq)
            seq.pop()

if __name__ == '__main__':
    dfs()