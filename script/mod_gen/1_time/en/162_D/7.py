def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            for k in range(j+1, N):
                if S[i] == S[k] or S[j] == S[k]:
                    continue
                if j - i == k - j:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()