def main():
    S = input()
    N = len(S)
    if N == 1:
        if int(S) % 2019 == 0:
            print(1)
        else:
            print(0)
        exit()
    else:
        S = S[::-1]
        S = [int(s) for s in S]
        #print(S)
        d = {}
        for i in range(N):
            d[i] = 0
        for i in range(N):
            d[i] = (d[i-1] + S[i] * pow(10, i, 2019)) % 2019
        #print(d)
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
                if (d[j] - d[i]) % 2019 == 0:
                    ans += 1
        print(ans)

if __name__ == '__main__':
    main()