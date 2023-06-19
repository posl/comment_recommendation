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
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum += (c[i] - b[i]) * a.count(b[i])
        print(sum)
        for j in range(n):
            if a[j] == b[i]:
                a[j] = c[i]
        #print(a)

if __name__ == '__main__':
    main()