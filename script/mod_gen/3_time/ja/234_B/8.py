def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    #print(x)
    #print(y)
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            length = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2)
            if max_length < length:
                max_length = length
    print(max_length)

if __name__ == '__main__':
    main()