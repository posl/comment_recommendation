def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_value = max(d.values())
    for key, value in sorted(d.items()):
        if value == max_value:
            print(key)

if __name__ == '__main__':
    main()