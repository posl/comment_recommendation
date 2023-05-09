def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        p = list(map(int, input().split()))
        P.append(p)
    for i in range(N):
        rank = 1
        for j in range(N):
            if P[i][0] + P[i][1] + P[i][2] < P[j][0] + P[j][1] + P[j][2]:
                rank += 1
        if rank <= K:
            print("Yes")
        else:
            print("No")
