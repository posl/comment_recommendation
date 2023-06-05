def main():
    n = int(input())
    p = []
    for i in range(n):
        x, y = map(int, input().split())
        p.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = p[i]
                x2, y2 = p[j]
                x3, y3 = p[k]
                s = abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))
                if s > 0 and s % 2 == 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()