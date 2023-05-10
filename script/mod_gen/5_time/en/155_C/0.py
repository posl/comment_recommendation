def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    max_num = max(d.values())
    for s in sorted(d):
        if d[s] == max_num:
            print(s)

if __name__ == '__main__':
    main()