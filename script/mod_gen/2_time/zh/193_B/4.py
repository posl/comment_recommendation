def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1, p1, x1 = map(int, input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    result = -1
    for i in range(n):
        if x[i] > 0:
            if result == -1:
                result = p[i]
            else:
                result = min(result, p[i])
    print(result)

if __name__ == '__main__':
    main()