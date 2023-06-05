def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x0, y0 = map(int, input().split())
        x.append(x0)
        y.append(y0)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] != x[j] and y[i] != y[j]:
                if x[i] in x and y[j] in y:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()