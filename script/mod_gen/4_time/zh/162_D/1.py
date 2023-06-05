def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R * G * B
    for i in range(N):
        for j in range(i+1,N):
            k = j * 2 - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()