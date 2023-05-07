def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    best = 0
    for i in range(N):
        if S[i] not in S[:i] and T[i] > T[best]:
            best = i
    print(best + 1)

if __name__ == '__main__':
    main()