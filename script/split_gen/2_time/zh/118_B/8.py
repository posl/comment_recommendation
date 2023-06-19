def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()[1:])))
    from itertools import combinations
    ans = 0
    for i in combinations(range(1, m+1), 1):
        for j in a:
            if not i[0] in j:
                break
        else:
            ans += 1
    print(ans)
