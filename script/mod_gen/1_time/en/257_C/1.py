def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i - 1] != S[i]:
            ans += 1
    print(ans + 1)
    return

if __name__ == '__main__':
    main()