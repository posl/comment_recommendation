def main():
    S = input()
    l = len(S)
    Q = S.count('?')
    ls = [0] * l
    for i in range(l):
        if S[i] == 'A':
            ls[i] = 1
        elif S[i] == 'B':
            ls[i] = 2
        elif S[i] == 'C':
            ls[i] = 3
    ans = 0
    for i in range(l):
        if ls[i] == 0:
            continue
        elif ls[i] == 1:
            ans += pow(3, Q, 10**9 + 7)
        elif ls[i] == 2:
            ans += pow(3, Q, 10**9 + 7) * pow(2, i, 10**9 + 7)
        elif ls[i] == 3:
            ans += pow(3, Q, 10**9 + 7) * pow(2, i, 10**9 + 7) * pow(2, i, 10**9 + 7)
        ans %= 10**9 + 7
    print(ans)

if __name__ == '__main__':
    main()