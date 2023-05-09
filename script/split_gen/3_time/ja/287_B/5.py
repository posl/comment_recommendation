def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    for i in range(N):
        cnt = 0
        for j in range(M):
            if S[i][-3:] == T[j]:
                cnt += 1
        print(cnt)
