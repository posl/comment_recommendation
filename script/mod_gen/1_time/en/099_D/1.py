def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    C1, C2, C3 = [], [], []
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1.append(c[i][j])
            elif (i + j) % 3 == 1:
                C2.append(c[i][j])
            else:
                C3.append(c[i][j])
    D1, D2, D3 = [0]*C, [0]*C, [0]*C
    for i in range(C):
        for j in range(C):
            D1[i] += D[i][j]*C1.count(j+1)
            D2[i] += D[i][j]*C2.count(j+1)
            D3[i] += D[i][j]*C3.count(j+1)
    ans = 10**10
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, D1[i] + D2[j] + D3[k])
    print(ans)

if __name__ == '__main__':
    main()