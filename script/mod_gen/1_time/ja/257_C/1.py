def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()