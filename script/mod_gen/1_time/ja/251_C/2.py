def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    ans = 0
    max = 0
    for i in range(N):
        for j in range(i):
            if S[i] == S[j]:
                break
        else:
            if T[i] > max:
                ans = i + 1
                max = T[i]
    print(ans)

if __name__ == '__main__':
    main()