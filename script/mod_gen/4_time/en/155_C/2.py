def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    max = 0
    for i in d:
        if max < d[i]:
            max = d[i]
    for i in sorted(d):
        if d[i] == max:
            print(i)

if __name__ == '__main__':
    main()