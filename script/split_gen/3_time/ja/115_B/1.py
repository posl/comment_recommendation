def main():
    N = int(input())
    P = []
    for i in range(N):
        P.append(int(input()))
    P.sort()
    P[N-1] = int(P[N-1] / 2)
    print(sum(P))
