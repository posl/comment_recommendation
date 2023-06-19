def main():
    N = int(input())
    seqs = []
    for i in range(N):
        seq = list(map(int, input().split()))
        seqs.append(seq[1:])
    seqs.sort()
    ans = 1
    for i in range(1, N):
        if seqs[i] != seqs[i - 1]:
            ans += 1
    print(ans)
main()
