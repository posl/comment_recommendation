def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    #print(d)
    m = max(d.values())
    #print(m)
    for k in sorted(d.keys()):
        if d[k] == m:
            print(k)

if __name__ == '__main__':
    main()