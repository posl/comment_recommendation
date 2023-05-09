def main():
    N, M = map(int, input().split())
    kx = []
    for i in range(M):
        kx.append(list(map(int, input().split())))
    ans = "Yes"
    for i in range(M):
        for j in range(i+1, M):
            if len(set(kx[i][1:]) & set(kx[j][1:])) == 0:
                ans = "No"
                break
    print(ans)
