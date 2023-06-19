def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b1, c1 = map(int, input().split())
        b.append(b1)
        c.append(c1)
    s = sum(a)
    for i in range(q):
        s = s + (c[i] - b[i]) * a.count(b[i])
        print(s)

if __name__ == '__main__':
    main()