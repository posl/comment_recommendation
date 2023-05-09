def main():
    N = int(input())
    seqs = [list(map(int, input().split())) for _ in range(N)]
    print(len(set(tuple(seq[1:]) for seq in seqs)))
