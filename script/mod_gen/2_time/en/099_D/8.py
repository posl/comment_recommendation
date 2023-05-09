def main():
    #input
    N, C = map(int, input().split())
    D = [[int(i) for i in input().split()] for _ in range(C)]
    c = [[int(i) for i in input().split()] for _ in range(N)]
    #solve
    ans = 10**15
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                cost = 0
                for l in range(N):
                    for m in range(N):
                        if (l+m) % 3 == 0:
                            cost += D[c[l][m]-1][i]
                        elif (l+m) % 3 == 1:
                            cost += D[c[l][m]-1][j]
                        else:
                            cost += D[c[l][m]-1][k]
                ans = min(ans, cost)
    #print
    print(ans)

if __name__ == '__main__':
    main()