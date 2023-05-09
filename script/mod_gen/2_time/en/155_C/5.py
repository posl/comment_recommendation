def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    max_value = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_value:
            print(k)
main()

if __name__ == '__main__':
    main()