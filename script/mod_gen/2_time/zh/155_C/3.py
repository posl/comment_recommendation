def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max = 0
    for i in range(N):
        if S[i] != S[i-1]:
            count = S.count(S[i])
            if max < count:
                max = count
    for i in range(N):
        if S[i] != S[i-1]:
            count = S.count(S[i])
            if max == count:
                print(S[i])

if __name__ == '__main__':
    main()