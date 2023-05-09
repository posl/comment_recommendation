def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    maxScore = max(T)
    maxScoreIndex = T.index(maxScore)
    print(S[maxScoreIndex])
