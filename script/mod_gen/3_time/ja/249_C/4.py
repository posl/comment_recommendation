def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** N):
        bin_i = bin(i)[2:]
        bin_i = '0' * (N - len(bin_i)) + bin_i
        bin_i = bin_i[::-1]
        tmp = ''
        for j in range(N):
            if bin_i[j] == '1':
                tmp += S[j]
        tmp = sorted(tmp)
        cnt = 0
        for j in range(len(tmp) - 1):
            if tmp[j] == tmp[j + 1]:
                cnt += 1
        if cnt == K:
            ans = max(ans, len(set(tmp)))
    print(ans)

if __name__ == '__main__':
    main()