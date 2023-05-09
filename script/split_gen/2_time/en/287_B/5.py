def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    result = 0
    for i in range(N):
        for j in range(M):
            if S[i][3:6] == T[j]:
                result += 1
    print(result)
main()
