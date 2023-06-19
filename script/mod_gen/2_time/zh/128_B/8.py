def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, p = input().split()
        p = int(p)
        if s in d:
            d[s].append(p)
        else:
            d[s] = [p]
    for k in sorted(d.keys()):
        for v in sorted(d[k], reverse=True):
            print(v)

if __name__ == '__main__':
    main()