def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    p = 0
    q = 0
    for i in range(1, N+1):
        for j in range(N-i):
            if P[j] > P[j+1]:
                P[j], P[j+1] = P[j+1], P[j]
                p += 1
            if Q[j] > Q[j+1]:
                Q[j], Q[j+1] = Q[j+1], Q[j]
                q += 1
    print(abs(p - q))
