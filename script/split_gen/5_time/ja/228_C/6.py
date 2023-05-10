def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    P_sum = []
    for i in range(N):
        P_sum.append(sum(P[i]))
    P_sum.sort(reverse=True)
    for i in range(N):
        if P_sum[i] >= P_sum[K-1]:
            print("Yes")
        else:
            print("No")
