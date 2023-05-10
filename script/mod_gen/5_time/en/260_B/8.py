def main():
    # Get input
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Sort by score
    c = []
    for i in range(n):
        c.append([i + 1, a[i], b[i]])
    c.sort(key=lambda x: x[1] + x[2], reverse=True)
    # Admit
    d = []
    for i in range(x):
        d.append(c[i][0])
    for i in range(x, x + y):
        d.append(c[i][0])
    for i in range(x + y, x + y + z):
        d.append(c[i][0])
    d.sort()
    # Print output
    for i in range(len(d)):
        print(d[i])

if __name__ == '__main__':
    main()