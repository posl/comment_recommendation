def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    min = 1000000000
    min_index = 0
    for i in range(N):
        if S[i] not in S[:i]:
            if T[i] < min:
                min = T[i]
                min_index = i
    print(min_index + 1)

if __name__ == '__main__':
    main()