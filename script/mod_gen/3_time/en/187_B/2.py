def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(n):
        for j in range(i):
            if abs(x[i] - x[j]) <= abs(y[i] - y[j]):
                count += 1
    print(count)

if __name__ == '__main__':
    main()