def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W = sorted(W)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += N - i
        else:
            ans += i
    print(ans)
main()

if __name__ == '__main__':
    main()