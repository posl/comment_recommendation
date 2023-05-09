def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for l in range(n):
                if l == i or l == j:
                    continue
                for m in range(n):
                    if m == i or m == j or m == l:
                        continue
                    for o in range(n):
                        if o == i or o == j or o == l or o == m:
                            continue
                        for p in range(n):
                            if p == i or p == j or p == l or p == m or p == o:
                                continue
                            for q in range(n):
                                if q == i or q == j or q == l or q == m or q == o or q == p:
                                    continue
                                if t[i][j] + t[j][l] + t[l][m] + t[m][o] + t[o][p] + t[p][q] + t[q][i] == k:
                                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()