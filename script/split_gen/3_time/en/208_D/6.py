def main():
    N, M = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            for k in range(1, N + 1):
                if s == t:
                    ans += 0
                else:
                    min_cost = 10**6 * N
                    for a, b, c in road:
                        if a > k:
                            continue
                        if a == s and b == t:
                            min_cost = min(min_cost, c)
                        elif a == s:
                            min_cost = min(min_cost, c + 0)
                    if min_cost == 10**6 * N:
                        ans += 0
                    else:
                        ans += min_cost
    print(ans)
    return
