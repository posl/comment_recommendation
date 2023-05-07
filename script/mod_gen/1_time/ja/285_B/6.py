def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        ans = 0
        for j in range(i):
            if S[j] != S[j + i]:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()