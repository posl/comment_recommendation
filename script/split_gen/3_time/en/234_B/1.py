def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            length = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**(1/2)
            if length > max_length:
                max_length = length
    print(max_length)
