def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                cnt += 1
    print(R*G*B - cnt)

if __name__ == '__main__':
    main()