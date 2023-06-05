def main():
    num = int(input())
    a = []
    p = []
    x = []
    for i in range(num):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min = 10**9
    for i in range(num):
        if x[i] > 0:
            if p[i] < min:
                min = p[i]
    if min == 10**9:
        print(-1)
    else:
        print(min)

if __name__ == '__main__':
    main()