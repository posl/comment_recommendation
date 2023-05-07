def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    count = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                count += 1
    print(count)
