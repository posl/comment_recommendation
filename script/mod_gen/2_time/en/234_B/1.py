def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    max = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                l = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
                if l > max:
                    max = l
    print(max)

if __name__ == '__main__':
    main()