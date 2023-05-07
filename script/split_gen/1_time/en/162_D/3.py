def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    ans = R*G*B
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] != S[j]:
                if 2*j-i < N:
                    if S[i] != S[2*j-i] and S[j] != S[2*j-i]:
                        ans -= 1
                if j+i < N and j+i < 2*j-i:
                    if S[i] != S[j+i] and S[j] != S[j+i]:
                        ans -= 1
                if j-i < N and j-i < 2*j-i:
                    if S[i] != S[j-i] and S[j] != S[j-i]:
                        ans -= 1
    print(ans)
main()
