def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    score = 0
    for i in range(N):
        if T[i] == "r":
            if i >= K:
                if T[i-K] == "r":
                    T[i] = "x"
                else:
                    score += P
            else:
                score += P
        elif T[i] == "s":
            if i >= K:
                if T[i-K] == "s":
                    T[i] = "x"
                else:
                    score += R
            else:
                score += R
        else:
            if i >= K:
                if T[i-K] == "p":
                    T[i] = "x"
                else:
                    score += S
            else:
                score += S
    print(score)

if __name__ == '__main__':
    main()