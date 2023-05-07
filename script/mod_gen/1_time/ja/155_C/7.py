def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        d[s] = d.get(s, 0) + 1
    max_v = max(d.values())
    for k, v in d.items():
        if v == max_v:
            print(k)

if __name__ == '__main__':
    main()