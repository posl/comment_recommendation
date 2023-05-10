def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            elif T[i] == "p":
                score += S
        else:
            if T[i] == "r":
                if T[i-K] == "r":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    score += P
            elif T[i] == "s":
                if T[i-K] == "s":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    score += R
            elif T[i] == "p":
                if T[i-K] == "p":
                    T = T[:i] + "x" + T[i+1:]
                else:
                    score += S
    print(score)
