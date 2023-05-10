def main():
    N, X = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "o":
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(X+ans)

if __name__ == '__main__':
    main()