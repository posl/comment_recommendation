def main():
    n = int(input())
    seqs = []
    for _ in range(n):
        seqs.append(input().split())
    seqs.sort()
    prev = seqs[0]
    cnt = 1
    for seq in seqs[1:]:
        if seq != prev:
            cnt += 1
        prev = seq
    print(cnt)
