def main():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == "A":
            for j in range(i+1, N):
                if S[j] == "B":
                    for k in range(j+1, N):
                        if S[k] == "C":
                            ans += 1
    print(ans % mod)

if __name__ == '__main__':
    main()