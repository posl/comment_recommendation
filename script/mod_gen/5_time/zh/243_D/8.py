def main():
    N,X = map(int,input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'U':
            ans = (ans + 1) // 2
        elif S[i] == 'L':
            ans = 2 * ans - 1
        else:
            ans = 2 * ans + 1
    print(ans)

if __name__ == '__main__':
    main()