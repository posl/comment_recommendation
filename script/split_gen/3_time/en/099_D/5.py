def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(C)]
    c = [list(map(int, input().split())) for i in range(N)]
    c1 = []
    c2 = []
    c3 = []
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                c1.append(c[i][j])
            elif (i + j) % 3 == 1:
                c2.append(c[i][j])
            else:
                c3.append(c[i][j])
    cost1 = [0] * C
    cost2 = [0] * C
    cost3 = [0] * C
    for i in range(C):
        for j in c1:
            cost1[i] += D[j - 1][i]
        for j in c2:
            cost2[i] += D[j - 1][i]
        for j in c3:
            cost3[i] += D[j - 1][i]
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, cost1[i] + cost2[j] + cost3[k])
    print(ans)
