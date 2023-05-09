def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in d:
            d[s].append(t)
        else:
            d[s] = [t]
    for k, v in d.items():
        d[k] = sorted(v, reverse=True)
    # print(d)
    d = sorted(d.items(), key=lambda x: x[1][0], reverse=True)
    # print(d)
    print(d[0][1][1])

if __name__ == '__main__':
    main()