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
            else:
                score += S
        else:
            if T[i] == T[i - K]:
                T[i] = "x"
            elif T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
    print(score)
