def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[i] - y[j])/(x[i] - x[j]) <= 1:
                count += 1
    print(count)
