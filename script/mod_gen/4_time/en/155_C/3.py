def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    m = max(d.values())
    for k, v in sorted(d.items()):
        if v == m:
            print(k)

if __name__ == '__main__':
    main()