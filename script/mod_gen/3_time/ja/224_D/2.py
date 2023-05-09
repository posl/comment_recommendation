def main():
    M = int(input())
    graph = [[] for i in range(9)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    p = list(map(int, input().split()))
    for i in range(8):
        p[i] -= 1
    ans = 10**9
    for i in range(8):
        for j in range(8):
            if i == j:
                continue
            for k in range(8):
                if i == k or j == k:
                    continue
                for l in range(8):
                    if i == l or j == l or k == l:
                        continue
                    for m in range(8):
                        if i == m or j == m or k == m or l == m:
                            continue
                        for n in range(8):
                            if i == n or j == n or k == n or l == n or m == n:
                                continue
                            for o in range(8):
                                if i == o or j == o or k == o or l == o or m == o or n == o:
                                    continue
                                for q in range(8):
                                    if i == q or j == q or k == q or l == q or m == q or n == q or o == q:
                                        continue
                                    for r in range(8):
                                        if i == r or j == r or k == r or l == r or m == r or n == r or o == r or q == r:
                                            continue
                                        for s in range(8):
                                            if i == s or j == s or k == s or l == s or m == s or n == s or o == s or q == s or r == s:
                                                continue
                                            for t in range(8):
                                                if i == t or j == t or k == t or l == t or m == t or n == t or o == t or q == t or r == t or s == t:
                                                    continue
                                                for u in range(8):
                                                    if i == u or j == u or k == u or l == u or m == u or n == u or o == u or q == u or r == u or s

if __name__ == '__main__':
    main()