def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        d[s] = d.get(s, 0) + 1
    max_count = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_count:
            print(k)

if __name__ == '__main__':
    main()