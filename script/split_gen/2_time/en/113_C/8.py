def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]
    cities.sort(key=lambda x: x[1])
    
    ans = [0] * M
    pref = [0] * (N + 1)
    for i, (p, y) in enumerate(cities):
        pref[p] += 1
        ans[i] = '{:06}{:06}'.format(p, pref[p])
    
    print(*ans, sep='
')
main()
