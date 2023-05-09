def main():
    n = int(input())
    seqs = []
    for i in range(n):
        seq = list(map(int, input().split()))
        seqs.append(seq[1:])
    seqs.sort()
    count = 1
    for i in range(1, n):
        if seqs[i] != seqs[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()