def main():
    N, M = map(int, input().split())
    # print(N, M)
    k = []
    x = []
    for i in range(M):
        k.append(input().split())
        # print(k[i])
        x.append(k[i][1:])
        # print(x[i])
    # print(x)
    ans = "No"
    for i in range(M):
        for j in range(i+1, M):
            if len(set(x[i]) & set(x[j])) > 0:
                ans = "Yes"
    print(ans)
