def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 10
        else:
            if S[i] == S[i-1]:
                ans += 10
            else:
                ans += 10 - 1
    print(ans)
main()

if __name__ == '__main__':
    main()