def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dist = ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
            if dist > max:
                max = dist
    print(max)
