def main():
    S = input()
    Q = S.count('?')
    A = 0
    B = 0
    C = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A -= 1
        elif S[i] == 'B':
            B -= 1
        elif S[i] == 'C':
            C -= 1
        elif S[i] == '?':
            if A == 0:
                ans += pow(3,Q,1000000007) * C
                C -= 1
            elif B == 0:
                ans += pow(3,Q,1000000007) * C
                C -= 1
            elif C == 0:
                ans += pow(3,Q,1000000007) * B
                B -= 1
            else:
                ans += pow(3,Q,1000000007) * (A + B + C)
                A -= 1
                B -= 1
                C -= 1
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()