def main():
    S = input()
    K = int(input())
    N = len(S)
    Xs = []
    for i in range(N):
        if S[i] == 'X':
            if i == 0 or S[i-1] != 'X':
                Xs.append(0)
            Xs[-1] += 1
    ans = 0
    for i in range(len(Xs)):
        ans += Xs[i]
        if K >= Xs[i]:
            K -= Xs[i]
            ans += K
            break
    print(ans)
main()

if __name__ == '__main__':
    main()