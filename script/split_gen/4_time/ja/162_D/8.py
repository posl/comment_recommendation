def main():
    N = int(input())
    S = input()
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    #print(R,G,B)
    ans = R * G * B
    #print(ans)
    for i in range(N):
        for j in range(i+1,N):
            k = j + (j-i)
            if k >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)
