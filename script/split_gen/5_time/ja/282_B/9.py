def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    count += 1
                    break
    print(count)
