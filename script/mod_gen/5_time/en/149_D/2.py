def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if T[i] == 'r':
            if i >= K and T[i-K] == 'r':
                T = T[:i] + 'x' + T[i+1:]
            else:
                score += P
        elif T[i] == 's':
            if i >= K and T[i-K] == 's':
                T = T[:i] + 'x' + T[i+1:]
            else:
                score += R
        else:
            if i >= K and T[i-K] == 'p':
                T = T[:i] + 'x' + T[i+1:]
            else:
                score += S
    print(score)

if __name__ == '__main__':
    main()