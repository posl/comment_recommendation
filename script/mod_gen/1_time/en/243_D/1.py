def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans * 2
        elif S[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = ans * 2 + 1
    print(ans)

if __name__ == '__main__':
    main()