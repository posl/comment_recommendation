def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j]:
                continue
            for k in range(j+1, n):
                if y[i] == y[k]:
                    continue
                if x[k] == x[j]:
                    continue
                if y[j] == y[k]:
                    continue
                if x[i] == x[k]:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()