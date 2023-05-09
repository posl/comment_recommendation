def main():
    N, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x:x[1])
    ans = "Yes"
    for i in range(N):
        if P[i][2] > W:
            ans = "No"
            break
        W -= P[i][2]
        for j in range(i+1, N):
            if P[i][1] <= P[j][0]:
                break
            if P[i][1] < P[j][1]:
                P[j][2] -= min(P[j][2], P[i][2])
        if W == 0:
            break
    print(ans)

if __name__ == '__main__':
    main()