def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    best = max(T)
    best_i = T.index(best)
    print(S[best_i])

if __name__ == '__main__':
    main()