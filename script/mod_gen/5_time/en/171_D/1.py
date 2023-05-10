def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    s = sum(a)
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for b, c in bc:
        if b in d:
            s += (c - b) * d[b]
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            del d[b]
        print(s)

if __name__ == '__main__':
    main()