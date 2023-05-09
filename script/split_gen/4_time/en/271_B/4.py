def main():
    N, Q = map(int, input().split())
    seqs = []
    for i in range(N):
        seqs.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(seqs[s-1][t-1])
