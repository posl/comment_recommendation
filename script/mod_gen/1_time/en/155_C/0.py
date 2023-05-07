def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_count = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_count:
            print(k)

if __name__ == '__main__':
    main()