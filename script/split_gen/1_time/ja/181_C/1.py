def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if x[i] == x[j] and x[j] == x[k]:
                    print("Yes")
                    return
                elif y[i] == y[j] and y[j] == y[k]:
                    print("Yes")
                    return
                elif (y[j] - y[i]) * (x[k] - x[i]) == (y[k] - y[i]) * (x[j] - x[i]):
                    print("Yes")
                    return
    print("No")
    return
