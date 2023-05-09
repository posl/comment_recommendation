def main():
    S = input()
    MOD = 2019
    ans = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if int(S[i:j]) % MOD == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()