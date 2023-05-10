def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A -= 1
        elif S[i] == 'B':
            B -= 1
        elif S[i] == 'C':
            C -= 1
        else:
            ans += A*(pow(3,Q,1000000007) + 3*pow(3,Q-1,1000000007) + 3*pow(3,Q-1,1000000007))
            ans += B*(pow(3,Q,1000000007) + 3*pow(3,Q-1,1000000007))
            ans += C*pow(3,Q,1000000007)
    ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()