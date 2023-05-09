def main():
    N = int(input())
    S = input()
    r = S.count('R')
    g = S.count('G')
    b = S.count('B')
    ans = r * g * b
    for i in range(N):
        for j in range(i + 1, N):
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()