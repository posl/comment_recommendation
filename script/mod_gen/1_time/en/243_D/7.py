def main():
    N,X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans - 1
        elif S[i] == 'R':
            ans = ans + 1
        elif S[i] == 'U':
            ans = ans // 2
    print(ans)
main()

if __name__ == '__main__':
    main()