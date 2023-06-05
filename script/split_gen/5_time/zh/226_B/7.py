def main():
    import sys
    N = int(sys.stdin.readline().strip())
    seqs = []
    for i in range(N):
        seq = sys.stdin.readline().strip().split()
        seqs.append(seq[1:])
    print(len(set(tuple(seq) for seq in seqs)))
