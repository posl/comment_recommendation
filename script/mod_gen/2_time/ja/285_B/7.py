def main():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for j in range(i):
            if S[j] != S[j + i]:
                ans[i - 1] += 1
    for i in range(N - 1):
        print(ans[i])

if __name__ == '__main__':
    main()