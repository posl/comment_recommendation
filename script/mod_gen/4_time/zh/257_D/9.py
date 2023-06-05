def main():
    n = int(input())
    x = []
    y = []
    p = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        p.append(c)
    s = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if p[i]*s >= abs(x[i]-x[j])+abs(y[i]-y[j]):
                break
        else:
            s += 1
    print(s)

if __name__ == '__main__':
    main()