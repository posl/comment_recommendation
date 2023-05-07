def main():
    S = input()
    mod = 10**9 + 7
    Q = S.count('?')
    n = len(S)
    ABC = [0]*n
    ABC[0] = 1
    for i in range(1,n):
        if S[i-1] == '?':
            ABC[i] = ABC[i-1]*3
        else:
            ABC[i] = ABC[i-1]
    print(ABC)
    ans = 0
    for i in range(n):
        if S[i] == 'A':
            ans += ABC[i]*pow(3,Q,mod)
        elif S[i] == 'B':
            ans += ABC[i]*pow(3,Q,mod)
        elif S[i] == 'C':
            ans += ABC[i]*pow(3,Q,mod)
        elif S[i] == '?':
            ans += ABC[i]*pow(3,Q-1,mod)
    print(ans%mod)

if __name__ == '__main__':
    main()