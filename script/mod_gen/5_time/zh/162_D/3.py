def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                    ans += 1
    print(R*G*B - ans)

if __name__ == '__main__':
    main()