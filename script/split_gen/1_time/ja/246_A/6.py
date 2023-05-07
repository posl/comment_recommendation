def main():
    x = []
    y = []
    for i in range(3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(3):
        if x.count(x[i]) == 1:
            x = x[i]
            break
    for i in range(3):
        if y.count(y[i]) == 1:
            y = y[i]
            break
    print(x, y)
