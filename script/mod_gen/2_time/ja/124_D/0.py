def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            for j in range(i, N):
                if S[j] == '1':
                    ans = max(ans, j-i)
                    break
            else:
                ans = max(ans, N-i)
                break
        elif S[i] == '1':
            for j in range(i, N):
                if S[j] == '0':
                    ans = max(ans, j-i)
                    break
            else:
                ans = max(ans, N-i)
                break
    print(ans+K-1)

if __name__ == '__main__':
    main()