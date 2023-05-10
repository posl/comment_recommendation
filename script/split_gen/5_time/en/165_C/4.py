def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    ans = 0
    for a in range(1, m+1):
        for b in range(a, m+1):
            for c in range(b, m+1):
                for d in range(c, m+1):
                    for e in range(d, m+1):
                        for f in range(e, m+1):
                            for g in range(f, m+1):
                                for h in range(g, m+1):
                                    for i in range(h, m+1):
                                        for j in range(i, m+1):
                                            l = [a, b, c, d, e, f, g, h, i, j]
                                            tmp = 0
                                            for k in range(q):
                                                if l[abcd[k][1]-1] - l[abcd[k][0]-1] == abcd[k][2]:
                                                    tmp += abcd[k][3]
                                            if tmp > ans:
                                                ans = tmp
    print(ans)
