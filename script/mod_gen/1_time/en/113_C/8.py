def main():
    n, m = map(int, input().split())
    # city list
    city = [list(map(int, input().split())) for _ in range(m)]
    # city list by prefecture
    city_by_pref = [[] for _ in range(n)]
    for i, c in enumerate(city):
        city_by_pref[c[0] - 1].append([i, c[1]])
    # sort city list by prefecture
    for p in city_by_pref:
        p.sort(key=lambda x: x[1])
    # output
    for p in city_by_pref:
        for i, c in enumerate(p):
            print("{:0=6}{:0=6}".format(c[1], i + 1))

if __name__ == '__main__':
    main()