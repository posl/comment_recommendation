def main():
    import sys
    input = sys.stdin.readline
    K = int(input())
    S = input().rstrip()
    T = input().rstrip()
    Takahashi = [0]*10
    Aoki = [0]*10
    for i in range(4):
        Takahashi[int(S[i])] += 1
        Aoki[int(T[i])] += 1
    
    Takahashi[0] = K - sum(Takahashi)
    Aoki[0] = K - sum(Aoki)
    Takahashi_score = 0
    for i in range(1,10):
        Takahashi_score += i * 10**(Takahashi[i])
    Aoki_score = 0
    for i in range(1,10):
        Aoki_score += i * 10**(Aoki[i])
    Takahashi_win = 0
    for i in range(1,10):
        if Takahashi[i] == K:
            continue
        Takahashi[i] += 1
        for j in range(1,10):
            if Aoki[j] == K:
                continue
            Aoki[j] += 1
            if (Takahashi_score + i*10**(Takahashi[0]-1)) > (Aoki_score + j*10**(Aoki[0]-1)):
                Takahashi_win += (Takahashi[i]-1)*(Aoki[j]-1)
            Aoki[j] -= 1
        Takahashi[i] -= 1
    
    print(Takahashi_win/(9*K-8)/(8*K-8))
