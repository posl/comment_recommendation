def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    ans = 0
    max_score = 0
    for i in range(N):
        if S[i] not in S[:i]:
            if T[i] > max_score:
                max_score = T[i]
                ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()