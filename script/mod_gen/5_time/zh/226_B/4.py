def main():
    N = int(input())
    seqs = []
    for i in range(N):
        seqs.append(list(map(int, input().split()[1:])))
    seqs.sort()
    # print(seqs)
    ans = 1
    for i in range(N-1):
        if seqs[i] != seqs[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()