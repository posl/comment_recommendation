def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    from itertools import combinations
    ans = 0
    for a, b, c in combinations(range(1, N + 1), 3):
        for u, v in edges:
            if {a, b} == {u, v} or {b, c} == {u, v} or {c, a} == {u, v}:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()