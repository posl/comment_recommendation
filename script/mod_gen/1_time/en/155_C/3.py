def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    d = {}
    for s in S:
        d[s] = d.get(s, 0) + 1
    max_count = max(d.values())
    for s in d:
        if d[s] == max_count:
            print(s)

if __name__ == '__main__':
    main()