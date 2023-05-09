def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R * G * B
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == S[j]:
                continue
            k = j + (j - i)
            if k >= N:
                continue
            if S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()