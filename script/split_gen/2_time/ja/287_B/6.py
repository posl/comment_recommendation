def main():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    count = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                count += 1
    print(count)
