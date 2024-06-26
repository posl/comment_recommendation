def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_val = max(d.values())
    for k, v in d.items():
        if v == max_val:
            print(k)

if __name__ == '__main__':
    main()