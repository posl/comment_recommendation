def main():
    N = int(input())
    S = [input().split() for _ in range(N)]
    for i in range(N):
        S[i][1] = int(S[i][1])
    S.sort(key=lambda x: x[0])
    S.sort(key=lambda x: x[1], reverse=True)
    for i in range(N):
        print(S[i][0])

if __name__ == '__main__':
    main()