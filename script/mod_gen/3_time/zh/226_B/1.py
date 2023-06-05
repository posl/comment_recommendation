def main():
    n = int(input())
    seqs = {}
    for i in range(n):
        seq = tuple(map(int, input().split()[1:]))
        if seq not in seqs:
            seqs[seq] = 1
        else:
            seqs[seq] += 1
    print(len(seqs))

if __name__ == '__main__':
    main()