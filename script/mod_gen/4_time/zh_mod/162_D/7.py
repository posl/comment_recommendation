def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()