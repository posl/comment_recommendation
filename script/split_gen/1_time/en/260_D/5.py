def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        P[i] -= 1
    eaten = [False] * N
    table = [0] * N
    table[0] = P[0]
    eaten[P[0]] = True
    top = 0
    for i in range(1, N):
        if P[i] > table[top]:
            top += 1
            table[top] = P[i]
            eaten[P[i]] = True
        else:
            j = 0
            while table[j] < P[i]:
                j += 1
            table[j] = P[i]
            eaten[P[i]] = True
    for i in range(N):
        if eaten[i]:
            for j in range(i + K - 1, N, K):
                eaten[j] = True
            for j in range(i - K + 1, -1, -K):
                eaten[j] = True
    for i in range(N):
        if eaten[i]:
            print(i + 1)
        else:
            print(-1)
