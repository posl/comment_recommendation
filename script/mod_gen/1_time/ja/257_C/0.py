def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    for i in range(N):
        if S[i] == '1':
            ans += 1
        else:
            ans -= 1
        ans = max(ans, 0)
    print(ans)

if __name__ == '__main__':
    main()