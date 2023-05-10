def main():
    # Get input
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Solve
    c = []
    for i in range(n):
        c.append([i+1, a[i], b[i], a[i]+b[i]])
    c.sort(key=lambda x: x[3], reverse=True)
    c.sort(key=lambda x: x[2], reverse=True)
    c.sort(key=lambda x: x[1], reverse=True)
    output = []
    for i in range(x):
        output.append(c[i][0])
    for i in range(y):
        output.append(c[i+x][0])
    for i in range(z):
        output.append(c[i+x+y][0])
    output.sort()
    # Print result
    for i in range(len(output)):
        print(output[i])
