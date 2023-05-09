def main():
    S = input()
    n = len(S)
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        if S[i] == 'c':
            for j in range(i+1,n):
                if S[j] == 'h':
                    for k in range(j+1,n):
                        if S[k] == 'o':
                            for l in range(k+1,n):
                                if S[l] == 'k':
                                    for m in range(l+1,n):
                                        if S[m] == 'u':
                                            for o in range(m+1,n):
                                                if S[o] == 'd':
                                                    for p in range(o+1,n):
                                                        if S[p] == 'a':
                                                            for q in range(p+1,n):
                                                                if S[q] == 'i':
                                                                    ans += 1
    print(ans%mod)

if __name__ == '__main__':
    main()